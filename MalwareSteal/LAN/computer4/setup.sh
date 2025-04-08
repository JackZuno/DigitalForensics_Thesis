#!/bin/bash

# Set up resolv.conf
echo "nameserver 8.8.8.8" > /etc/resolv.conf

# Routing
ip route del default via 10.20.0.254
route add default gw 10.20.0.253

ip route add 192.168.1.0/24 via 10.20.0.253 # Computer1 -> Server
ip route add 10.30.0.0/24 via 10.20.0.253 # Computer1 -> WLAN
ip route add 10.40.0.0/24 via 10.20.0.253 # Computer1 -> guest

# hostname resolution
echo "192.168.1.4 email_server" >> /etc/hosts
echo "192.168.1.2 database_server" >> /etc/hosts

# Add cron job to run the Python script every minute
CRON_JOB="* * * * * python3 /usr/local/bin/save_email.py"

# Check if the cron job is already in the crontab to avoid duplicates
(crontab -u jamesfoster -l | grep -F "$CRON_JOB") || (crontab -u jamesfoster -l 2>/dev/null; echo "$CRON_JOB") | crontab -u jamesfoster -

# Start crontab to run a python script
service cron start

source /usr/local/bin/db_setup.sh

# With these mutt will work
chown jamesfoster:jamesfoster /home/jamesfoster/sent
chown jamesfoster:jamesfoster /home/jamesfoster/inbox

# Other permissions to sarah
chown -R jamesfoster:jamesfoster /usr/local/bin
chown -R jamesfoster:jamesfoster /home/jamesfoster
chmod -R 755 /home/jamesfoster

# Keep the container running
tail -f /dev/null
