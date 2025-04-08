#!/bin/bash

# Set up DNS
echo "nameserver 8.8.8.8" > /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf

# Routing
ip route del default via 203.0.113.254
route add default gw 203.0.113.1

# ip route add 192.168.1.0/24 via 203.0.113.1 # Outside -> Server
# ip route add 10.20.0.0/24 via 203.0.113.1 # Outside -> LLAN
# ip route add 10.30.0.0/24 via 203.0.113.1 # Outside -> WLAN
# ip route add 10.40.0.0/24 via 203.0.113.1 # Outside -> guest

# hostname resolution for email_server
echo "192.168.1.4 email_server" >> /etc/hosts
echo "192.168.1.2 database_server" >> /etc/hosts

# With these mutt will work
chown elliotalderson:elliotalderson /home/elliotalderson/sent
chown elliotalderson:elliotalderson /home/elliotalderson/inbox

# Other permissions to sarah
chown -R elliotalderson:elliotalderson /usr/local/bin
chown -R elliotalderson:elliotalderson /home/elliotalderson
chmod -R 755 /home/elliotalderson

# Keep the container running
tail -f /dev/null