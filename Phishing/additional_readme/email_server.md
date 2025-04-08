## Email Server
In this configuration there is a local email server created to allow the exchange of emails between employees and also with people outside the company. 

### Users
On the email server a list of users is created, in order to have emails and related password. \
The creation of a user is done in this way:
```Dockerfile
# Create system users with specific UIDs and home directories
RUN adduser --gecos "" --home /home/sarahwilliams sarahwilliams && \
    echo "sarahwilliams:sarahwilliams" | chpasswd

# Dynamically get the uid and gid for user1 and user2
RUN uid1=$(id -u sarahwilliams) && gid1=$(id -g sarahwilliams) && \
    echo "sarahwilliams:{PLAIN}sarahwilliams:${uid1}:${gid1}::/home/sarahwilliams:/bin/false" >> /etc/dovecot/users

# Change ownership to dovecot user and group, and Set permissions for the user database file
RUN chown dovecot:dovecot /etc/dovecot/users && \
    chmod 640 /etc/dovecot/users

# Set up Postfix configurations
RUN sh -c 'echo "e-corp.com" >> /etc/mailname' && \
    sh -c 'echo "sarahwilliams@e-corp.com sarahwilliams" >> /etc/postfix/virtual' && \
    postmap /etc/postfix/virtual

# Ensure proper ownership and permissions for Postfix files
RUN chown root:root /etc/postfix/virtual /etc/postfix/virtual.db && \
    chmod 0600 /etc/postfix/virtual /etc/postfix/virtual.db
```
The login to a specific user is done using mutt, with the **.muttrc** configuration file. The configuration of muttrc depends on which port is used for IMAP and SMTP.\
An example of a **.muttrc** file:
```bash
# IMAP configuration
set imap_user = "sarahwilliams@e-corp.com"
set imap_pass = "sarahwilliams" 
set folder = "imaps://email_server:993"  # For non-TLS use port 143 (and remove the s from imaps -> imap)
set spoolfile = "+INBOX"
set header_cache = "~/.mutt/cache/headers"
set message_cachedir = "~/.mutt/cache/bodies"

# SMTP configuration
# set smtp_url = "smtps://sarahwilliams:sarahwilliams@email_server:465"  # If you do not want to use STARTTLS
set smtp_url = "smtp://sarahwilliams:sarahwilliams@email_server:587"  # STARTTLS
set smtp_pass = "sarahwilliams"  # Add SMTP password if required
set from = "sarahwilliams@e-corp.com"
set realname = "Sarah Williams"

set ssl_force_tls = yes  # Force TLS
set ssl_starttls = yes    # STARTTLS should be disabled for port 465 (set ssl_starttls = no)
```

### Server setup
The email server is made with **postfix** and **dovecot**, that are needed to make the server works, allowing it to send/receive emails. \
Dovecot primarily handles email retrieval and provides secure access to stored emails, while Postfix focuses on mail routing and delivery. \
Workflow examples:
- External email &rarr; Postfix (receives and processes) &rarr; Dovecot (stores in user mailbox)
- User connects via IMAP &rarr; Dovecot authenticates and provides email access
- User sends an email via its client &rarr; Postfix processes and delivers the email to recipient's mail server

#### Postfix
Postfix is a hugely-popular Mail Transfer Agent (**MTA**) designed to determine routes and send emails. \
In this case, Postfix uses port **587** for SMTP (Simple Mail Transfer Protocol) submission. This port is designated for sending outgoing emails from email clients to the mail server and is meant specifically for authenticated SMTP connections. The 587 port support STARTTLS, TLS encryption, which provides a secure channel for sending emails.\
The port **25** is the default one for SMTP and it does not require authentication by default. \
There is another port who supports TLS and it is the port **465**, but in this case it provides a secure way of sending emails by establishing an SSL/TLS encrypted connection from the very start of the communication. It is used for SMTPS (SMTP Secure). \
However, the port **465** was *deprecated* when STARTTLS became more popular, as STARTTLS allowed the standard Port 25 and Port 587 connections to be upgraded to encrypted connections without needing a dedicated port.

##### Postfix Configuration
For more information about Postfix configuration look here: **[postfix](email_server/postfix.md)**.

#### Dovecot
Dovecot is a high-performance mail delivery agent (**MDA**) with a focus on security. It manages email storage and provides access to emails for end users. Dovecot handles how users retrieve their emails from the server using the IMAP or POP3 protocols.\
In the email server I created I used IMAP with port 993.\
Port **143** is the default port for IMAP without encryption: when a client connects to the server using IMAP on this port, the communication between the client and the server is not encrypted by default. To secure communication on Port 143, STARTTLS can be used.\
Port **993** is the default port for IMAPS (IMAP Secure): it is used when encryption is required from the start of the connection. Unlike Port 143, when a client connects to Port 993, the communication is always encrypted using SSL/TLS. 

##### Dovecot Configuration
For more information about Dovecot configuration look here: **[dovecot](email_server/dovecot.md)**.

### Usage Client Side
On the computer that will use the email server, in addition to the muttrc file, you also need to add in the setup.sh file this command, so that the computer will know the address of the *email_server*:
```bash
echo "192.168.1.4 email_server" >> /etc/hosts
```

### Keys and Certificates
#### Generate
To generate the keys for the email server, you can use openssl:
```sh
# In my computer
openssl req -new -x509 -days 365 -nodes -out postfix.pem -keyout postfix.key
```
In this case, postfix will have a self signed certificate and the client will have the option to accept (once or always) the certificate or refuse to do it.

#### Copy Keys in The Email Server (Dockerfile)
Save the keys in the email_server using the Dockerfile:
```Dockerfile
# Copy the key certificate
COPY cert/postfix.pem /etc/ssl/certs/postfix.pem
COPY cert/postfix.key /etc/ssl/private/postfix.key
```

#### Test Keys (Client side)
To test the authentication for both IMAP and SMTP with SSL/TLS there are a sequence of openSSL commands:
```bash
# Test
openssl s_client -connect email_server:465
openssl s_client -connect email_server:993

# Test STARTTLS
openssl s_client -starttls smtp -connect email_server:587 -crlf
```

### Send Email
There are different ways to send a new email and I will talk about two of them.\
The *first method* is by opening mutt from command line and the following the instructions. This method is useful in case there are self signed certificates to accept, because you can manually accept/refuse them both time, when you open mutt (for dovecot) and when you send an email (for postfix).
```bash
# Open mutt
mutt

# Inside mutt
m # to send a new email (then follow instructions)
r # to reply to a specific email
d # to delete a specific email
q # to exit
```
The second option is to send the email from command line, with a single command (if you never have accepted the certificates there can be some problems):
```bash
# Inside the container of the sender
echo "Email body text" | mutt -s "Subject" receiver@e-corp.com

# With attachment
echo "Email body text" | mutt -s "Subject" -a /path/to/attachment -- receiver@e-corp.com
```
