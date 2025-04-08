#!/bin/bash

# Set up resolv.conf
echo "nameserver 8.8.8.8" > /etc/resolv.conf

# Routing
ip route del default via 10.30.0.254
ip route add default via 10.30.0.253

ip route add 192.168.1.0/24 via 10.30.0.253 # PC1 -> Server
ip route add 10.20.0.0/24 via 10.30.0.253   # PC1 -> LAN

# hostname resolution
echo "192.168.1.4 email_server" >> /etc/hosts
echo "192.168.1.2 database_server" >> /etc/hosts

# Add cron job to run the Python script every minute
CRON_JOB="* * * * * python3 /usr/local/bin/save_email.py"

# Check if the cron job is already in the crontab to avoid duplicates
(crontab -u annamoore -l | grep -F "$CRON_JOB") || (crontab -u annamoore -l 2>/dev/null; echo "$CRON_JOB") | crontab -u annamoore -

# Start crontab to run a python script
service cron start

source /usr/local/bin/db_setup.sh

# With these mutt will work
chown annamoore:annamoore /home/annamoore/sent
chown annamoore:annamoore /home/annamoore/inbox

# Other permissions to sarah
chown -R annamoore:annamoore /usr/local/bin
chown -R annamoore:annamoore /home/annamoore
chmod -R 755 /home/annamoore

# Keep the container running
tail -f /dev/null
