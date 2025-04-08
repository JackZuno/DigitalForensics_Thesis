#!/bin/bash

# Set up resolv.conf
echo "nameserver 8.8.8.8" > /etc/resolv.conf

# Routing
ip route del default via 10.20.0.254
route add default gw 10.20.0.253

ip route add 192.168.1.0/24 via 10.20.0.253 # computer2 -> server
ip route add 10.30.0.0/24 via 10.20.0.253   # computer2 -> WLAN
ip route add 10.40.0.0/24 via 10.20.0.253   # computer2 -> guest

# hostname resolution
echo "192.168.1.4 email_server" >> /etc/hosts
echo "192.168.1.2 database_server" >> /etc/hosts

# Add cron job to run the Python script every minute
CRON_JOB="* * * * * python3 /usr/local/bin/save_email.py"

# Check if the cron job is already in the crontab to avoid duplicates
(crontab -u johndoe -l | grep -F "$CRON_JOB") || (crontab -u johndoe -l 2>/dev/null; echo "$CRON_JOB") | crontab -u johndoe -

# Start crontab to run a python script
service cron start

# Add some files
echo "This is a great IDEA. I quit!" > /home/johndoe/files/brainer.txt
echo "I did a research about this and that." > /home/johndoe/files/research.txt
echo "My houses, addresses and other info." > /home/johndoe/files/personal.docx
echo "List of places." > /home/johndoe/files/places.docx
echo "This is a very complex contract that I made." > /home/johndoe/files/contract.txt

# With these mutt will work
chown johndoe:johndoe /home/johndoe/sent
chown johndoe:johndoe /home/johndoe/inbox

# Other permissions to sarah
chown -R johndoe:johndoe /usr/local/bin
chown -R johndoe:johndoe /home/johndoe
chmod -R 755 /home/johndoe

# Keep the container running
tail -f /dev/null
