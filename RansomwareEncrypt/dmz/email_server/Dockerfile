FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y mailutils postfix postfix-pcre && \
    apt-get install -y telnet nano net-tools rsyslog traceroute && \
    apt-get install -y dovecot-core dovecot-imapd dovecot-pop3d iputils-ping iproute2 iperf sudo faketime tshark

# Create system users with specific UIDs and home directories
RUN adduser --gecos "" --home /home/sarahwilliams sarahwilliams && \
    echo "sarahwilliams:sarahwilliams" | chpasswd && \
    adduser --gecos "" --home /home/johndoe johndoe && \
    echo "johndoe:johndoe" | chpasswd && \
    adduser --gecos "" --home /home/emilycarter emilycarter && \
    echo "emilycarter:emilycarter" | chpasswd && \
    adduser --gecos "" --home /home/sampointer sampointer && \
    echo "sampointer:sampointer" | chpasswd && \
    adduser --gecos "" --home /home/jamesfoster jamesfoster && \
    echo "jamesfoster:jamesfoster" | chpasswd && \
    adduser --gecos "" --home /home/jakethompson jakethompson && \
    echo "jakethompson:jakethompson" | chpasswd && \
    adduser --gecos "" --home /home/annamoore annamoore && \
    echo "annamoore:annamoore" | chpasswd && \
    adduser --gecos "" --home /home/oliviamurphy oliviamurphy && \
    echo "oliviamurphy:oliviamurphy" | chpasswd && \
    adduser --gecos "" --home /home/elliotalderson elliotalderson && \
    echo "elliotalderson:elliotalderson" | chpasswd

# Dynamically get the uid and gid for user1 and user2
RUN uid1=$(id -u sarahwilliams) && gid1=$(id -g sarahwilliams) && \
    uid2=$(id -u johndoe) && gid2=$(id -g johndoe) && \
    uid3=$(id -u emilycarter) && gid3=$(id -g emilycarter) && \
    uid4=$(id -u sampointer) && gid4=$(id -g sampointer) && \
    uid5=$(id -u jamesfoster) && gid5=$(id -g jamesfoster) && \
    uid6=$(id -u jakethompson) && gid6=$(id -g jakethompson) && \
    uid7=$(id -u annamoore) && gid7=$(id -g annamoore) && \
    uid8=$(id -u oliviamurphy) && gid8=$(id -g oliviamurphy) && \
    uid9=$(id -u elliotalderson) && gid9=$(id -g elliotalderson) && \
    echo "sarahwilliams:{PLAIN}sarahwilliams:${uid1}:${gid1}::/home/sarahwilliams:/bin/false" >> /etc/dovecot/users && \
    echo "johndoe:{PLAIN}johndoe:${uid2}:${gid2}::/home/johndoe:/bin/false" >> /etc/dovecot/users && \
    echo "emilycarter:{PLAIN}emilycarter:${uid3}:${gid3}::/home/emilycarter:/bin/false" >> /etc/dovecot/users && \
    echo "sampointer:{PLAIN}sampointer:${uid4}:${gid4}::/home/sampointer:/bin/false" >> /etc/dovecot/users && \
    echo "jamesfoster:{PLAIN}jamesfoster:${uid5}:${gid5}::/home/jamesfoster:/bin/false" >> /etc/dovecot/users && \
    echo "jakethompson:{PLAIN}jakethompson:${uid6}:${gid6}::/home/jakethompson:/bin/false" >> /etc/dovecot/users && \
    echo "annamoore:{PLAIN}annamoore:${uid7}:${gid7}::/home/annamoore:/bin/false" >> /etc/dovecot/users && \
    echo "oliviamurphy:{PLAIN}oliviamurphy:${uid8}:${gid8}::/home/oliviamurphy:/bin/false" >> /etc/dovecot/users && \
    echo "elliotalderson:{PLAIN}elliotalderson:${uid9}:${gid9}::/home/elliotalderson:/bin/false" >> /etc/dovecot/users

# Change ownership to dovecot user and group, and Set permissions for the user database file
RUN chown dovecot:dovecot /etc/dovecot/users && \
    chmod 640 /etc/dovecot/users

# Copy your custom configuration files into the container
COPY /10/10-ssl.conf /etc/dovecot/conf.d/10-ssl.conf
COPY /10/10-auth.conf /etc/dovecot/conf.d/10-auth.conf
COPY /10/10-logging.conf /etc/dovecot/conf.d/10-logging.conf
COPY /10/10-master.conf /etc/dovecot/conf.d/10-master.conf
COPY /20/20-imap.conf /etc/dovecot/conf.d/20-imap.conf
COPY /cf/auth-system.conf.ext /etc/dovecot/conf.d/auth-system.conf.ext
COPY /cf/main.cf /etc/postfix/main.cf
COPY /cf/master.cf /etc/postfix/master.cf

# Set up Postfix configurations
RUN sh -c 'echo "e-corp.com" >> /etc/mailname' && \
    sh -c 'echo "sarahwilliams@e-corp.com sarahwilliams" >> /etc/postfix/virtual' && \
    sh -c 'echo "johndoe@e-corp.com johndoe" >> /etc/postfix/virtual' && \
    sh -c 'echo "emilycarter@e-corp.com emilycarter" >> /etc/postfix/virtual' && \
    sh -c 'echo "sampointer@e-corp.com sampointer" >> /etc/postfix/virtual' && \
    sh -c 'echo "jamesfoster@e-corp.com jamesfoster" >> /etc/postfix/virtual' && \
    sh -c 'echo "jakethompson@e-corp.com jakethompson" >> /etc/postfix/virtual' && \
    sh -c 'echo "annamoore@e-corp.com annamoore" >> /etc/postfix/virtual' && \
    sh -c 'echo "oliviamurphy@e-corp.com oliviamurphy" >> /etc/postfix/virtual' && \
    sh -c 'echo "elliotalderson@mrrobot.com elliotalderson" >> /etc/postfix/virtual' && \
    postmap /etc/postfix/virtual

# Ensure proper ownership and permissions for Postfix files
RUN chown root:root /etc/postfix/virtual /etc/postfix/virtual.db && \
    chmod 0600 /etc/postfix/virtual /etc/postfix/virtual.db

# Copy the network configuration script
COPY server-config.sh /usr/local/bin/server-config.sh

# Make the script executable
RUN chmod +x /usr/local/bin/server-config.sh

# Copy the certificate and key
COPY cert/postfix.pem /etc/ssl/certs/postfix.pem
COPY cert/postfix.key /etc/ssl/private/postfix.key

# Copy the capture_traffic script and configuration files
COPY pythonScript/capture_traffic.py /usr/local/bin/capture_traffic.py
RUN chmod +x /usr/local/bin/capture_traffic.py

# Create directories for storing captures and logs
RUN mkdir -p /home/captureTraffic

# Run the script and keep the container alive
CMD ["/bin/bash", "-c", "/usr/local/bin/server-config.sh"]
