## Postfix Setup
### Main Configuration
In the file **main.cf**, there is the main configuration for postfix: in this file there are different things that are defined.\
In this file it is possible to set the hostname of the email server (**myhostanme**), the domain name that postfix will assume as the default for various settings (**mydomain**) and the destinations, which is the list of the domains that the server will accept emails from (**mydestination**), and if an email is addressed to any of these domains, Postfix will treat it as a local delivery and handle it accordingly. There is also the **relayhost**, which defines an optional relay server that Postfix can use to send all outgoing emails; leaving this blank means Postfix will deliver mail directly to the recipient's mail servers, rather than sending it to an intermediary (this is the case of this email server).

### Virtual Mailbox Configuration
In the file **main.cf**, there is the configuration for virtual mailbox:
```py
# This tells Postfix to listen for incoming mail on all network interfaces
inet_interfaces = all

# This allows Postfix to use both IPv4 and IPv6
inet_protocols = all

# This specifies domains for virtual mailboxes. Virtual mailboxes are used when email 
# accounts are not tied to system accounts. Postfix will accept mail for these domains 
# and route it to mailboxes in the specified directory (/var/mail).
virtual_mailbox_domains = localhost.localdomain, mrrobot.com

# This sets the base directory for the virtual mailboxes
virtual_mailbox_base = /var/mail

# This file maps email addresses to virtual mailboxes. Postfix uses this map to decide 
# where to deliver mail for virtual domains
virtual_mailbox_maps = hash:/etc/postfix/virtual

# This specifies an alias map for virtual domains, where you can define alias email addresses 
# that point to other mailboxes
virtual_alias_maps = hash:/etc/postfix/virtual
```

### SSL/TLS

#### SMTPS (465)
Inside the file **10-master.conf**, you need to remove the comment and insert the right port, in order to allow dovecot to deal with SMTP auth with SSL/TLS: 
```py
service submission-login {
  inet_listener submission {
    # port = 587
  }
  inet_listener submissions {
    port = 465
  }
}
```
There is something else to add inside the **10-master.conf** file. Postfix uses SMTP AUTH to authenticate clients before they are allowed to send mail. This requires Postfix to communicate with Dovecot to verify credentials, and this communication happens over a Unix socket. So, this block is creating a Unix socket at */var/spool/postfix/private/auth* which is used by Postfix to connect to Dovecot for authentication requests. The unix_listener directive is part of the Dovecot configuration that defines how Dovecot listens for authentication requests from Postfix. \
This sets the permissions on the socket file to 0666 (read and write for everyone), ensuring that Postfix can write to the socket to request authentication without permission issues. The user and group are both set to postfix, meaning the Postfix service is the one that is authorized to use this socket. \
When Postfix is configured to require SMTP authentication over SSL/TLS, it needs a secure way to pass credentials (like username and password) from the client to Dovecot for validation. This socket is how Postfix sends the credentials securely to Dovecot for checking.
```py
service auth {
  # Postfix smtp-auth
  unix_listener /var/spool/postfix/private/auth {
    mode = 0666
    user = postfix
    group = postfix  
  }
}
```
There are then some SSL/TLS settings to add in the **main.cf** file:
```py
# his points to the file containing the SSL/TLS certificate used by the Postfix 
# SMTP daemon to enable TLS encryption
smtpd_tls_cert_file=/etc/ssl/certs/postfix.pem

# This specifies the path to the private key corresponding to the certificate
smtpd_tls_key_file=/etc/ssl/private/postfix.key

# This tells Postfix to use TLS encryption if available, but it won't force encryption
smtpd_tls_security_level=may

# It points to the directory containing the Certificate Authority (CA) 
# certificates used to verify remote TLS certificates
smtp_tls_CApath=/etc/ssl/certs

# This sets TLS security for outbound SMTP communication. Postfix will 
# attempt TLS encryption for outgoing mail but won’t require it
smtp_tls_security_level=may

# This specifies a cache for storing session information, improving 
# the performance of TLS-encrypted sessions
smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache
```
Still in the **main.cf** file, there are some commands to add for SASL (Simple Authentication and Security Layer) Authentication, which is a  framework for authentication and data security in Internet protocols.
```py
# This tells Postfix to use Dovecot for SASL authentication
# This is needed for users to authenticate before sending mail through the SMTP server
smtpd_sasl_type = dovecot

# This specifies the path to the Dovecot authentication socket
smtpd_sasl_path = private/auth

# This is left blank, meaning that Postfix will not limit authentication to a specific domain
smtpd_sasl_local_domain =
```

Inside the **master.cf** file there are some part that must be added:
```py
# This one was already present
# smtps defines the service name, which is SMTP over SSL (commonly on port 465).
# inet specifies that the service is internet based; n means the service does not run 
# in a chroot jail.
# y allows Postfix to run the service as a foreground process and smtpd specifies that 
# Postfix will run the SMTP daemon (smtpd) to handle incoming mail on this service
smtps     inet  n       -       y       -       -       smtpd

  # The options starting with -o are overrides of the default Postfix settings

  # This option customizes the syslog name for logging
  -o syslog_name=postfix/smtps

  # SMTP connection is encrypted from the start, unlike STARTTLS which starts 
  # in plain text and then upgrades to TLS
  -o smtpd_tls_wrappermode=yes

  # This enables SASL authentication on this service
  -o smtpd_sasl_auth_enable=yes

  # This line defines the relay restrictions, which control who is allowed 
  # to relay (send) mail through the SMTP server
  # Permits users who have authenticated via SASL to send mail
  # Reject all other unauthenticated users who try to relay mail
  -o smtpd_relay_restrictions=permit_sasl_authenticated,reject
```

#### SMTP With STARTTLS (587)
To enable **STARTTLS** on the email server, there are some changes to do to the **master.cf** file:
```py
submission inet n       -       y       -       -       smtpd
  -o syslog_name=postfix/submission

  # Enables STARTTLS support, allowing clients to optionally use TLS
  -o smtpd_tls_security_level=may

  # Enables SASL authentication
  -o smtpd_sasl_auth_enable=yes

  # Requires TLS for authentication, ensuring the connection is encrypted
  -o smtpd_tls_auth_only=yes

  # Allows mail to be sent only by authenticated users and rejects others
  -o smtpd_recipient_restrictions=permit_sasl_authenticated,reject
  -o smtpd_relay_restrictions=permit_sasl_authenticated,reject

  # Helps in identifying mail coming from the submission port in logs
  -o milter_macro_daemon_name=ORIGINATING
```
Inside the **10-master.conf** file there is another change (Remove the comment to *port = 587*):
```py
service submission-login {
  inet_listener submission {
    port = 587
  }
  inet_listener submissions {
    port = 465
  }
}
```

### Logs Postfix
Inside the **main.cf** file it is possible to set the path for the logs:
```bash
# Log
maillog_file = /var/log/mail.log
```
To see the logs:
```bash
# Inside the email_server
tail -f var/log/mail.log
```
