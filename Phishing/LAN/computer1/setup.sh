#!/bin/bash

# Set up resolv.conf
echo "nameserver 8.8.8.8" > /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf

# Routing
ip route del default via 10.20.0.254
route add default gw 10.20.0.253

# These routes are not necessary
# ip route add 192.168.1.0/24 via 10.20.0.253 # Computer1 -> Server
# ip route add 10.30.0.0/24 via 10.20.0.253 # Computer1 -> WLAN
# ip route add 10.40.0.0/24 via 10.20.0.253 # Computer1 -> guest

# ip route add 203.0.113.0/24 via 10.20.0.253 # Computer1 -> outside

# hostname resolution
echo "192.168.1.4 email_server" >> /etc/hosts
echo "192.168.1.2 database_server" >> /etc/hosts

# Add cron job to run the Python script every minute
CRON_JOB="* * * * * python3 /usr/local/bin/save_email.py"

# Check if the cron job is already in the crontab to avoid duplicates
(crontab -u sarahwilliams -l | grep -F "$CRON_JOB") || (crontab -u sarahwilliams -l 2>/dev/null; echo "$CRON_JOB") | crontab -u sarahwilliams -

# Start crontab to run a python script
service cron start

# Add some files
echo "This is a great IDEA." > /home/sarahwilliams/new_ideas/brainer.txt
echo "I found this and that about this idea." > /home/sarahwilliams/new_ideas/research.txt
echo "It is good for these reasons, but it is not perfect because of these" > /home/sarahwilliams/new_ideas/pros_and_cons.docx
echo "It could look like this with these features" > /home/sarahwilliams/new_ideas/first_sketch.docx
echo "All these things are needed." > /home/sarahwilliams/new_ideas/info/details.txt
echo "The price is this and this for this and that." > /home/sarahwilliams/new_ideas/info/budget.docx
echo "We will need him for this, her for that and them for all this stuff." > /home/sarahwilliams/new_ideas/info/team.docx

# With these mutt will work
chown sarahwilliams:sarahwilliams /home/sarahwilliams/sent
chown sarahwilliams:sarahwilliams /home/sarahwilliams/inbox

source ./usr/local/bin/fake_history.sh

# Other permissions to sarah
chown -R sarahwilliams:sarahwilliams /usr/local/bin
chown -R sarahwilliams:sarahwilliams /home/sarahwilliams
chown -R sarahwilliams:sarahwilliams /networkCapture
chmod -R 755 /home/sarahwilliams

# Keep the container running
# tail -f /dev/null
