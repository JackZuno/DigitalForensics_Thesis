#!/bin/bash

# Set up resolv.conf
echo "nameserver 8.8.8.8" > /etc/resolv.conf

# Routing
ip route del default via 10.20.0.254
route add default gw 10.20.0.253

ip route add 192.168.1.0/24 via 10.20.0.253 # Computer3 -> Server
ip route add 10.30.0.0/24 via 10.20.0.253   # Computer3 -> WLAN
ip route add 10.40.0.0/24 via 10.20.0.253   # Computer3 -> guest

# hostname resolution
echo "192.168.1.4 email_server" >> /etc/hosts
echo "192.168.1.2 database_server" >> /etc/hosts

# Add cron job to run the Python script every minute
CRON_JOB="* * * * * python3 /usr/local/bin/save_email.py"

# Check if the cron job is already in the crontab to avoid duplicates
(crontab -u emilycarter -l | grep -F "$CRON_JOB") || (crontab -u emilycarter -l 2>/dev/null; echo "$CRON_JOB") | crontab -u emilycarter -

# Start crontab to run a python script
service cron start

# With these mutt will work
chown emilycarter:emilycarter /home/emilycarter/sent
chown emilycarter:emilycarter /home/emilycarter/inbox

# Other permissions to sarah
chown -R emilycarter:emilycarter /usr/local/bin
chown -R emilycarter:emilycarter /home/emilycarter
chmod -R 755 /home/emilycarter

# Keep the container running
tail -f /dev/null
