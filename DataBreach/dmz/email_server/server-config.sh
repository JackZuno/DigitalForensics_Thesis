#!/bin/bash

# Routing
ip route del default via 192.168.1.254
route add default gw 192.168.1.1

ip route add 10.20.0.0/24 via 192.168.1.1   # Email server -> LAN
ip route add 192.168.2.0/24 via 192.168.1.1 # Email server -> inside_router
ip route add 10.30.0.0/24 via 192.168.1.1   # Email server -> WLAN
ip route add 10.40.0.0/24 via 192.168.1.1   # Email server -> guest

ip route add 198.51.100.0/24 via 192.168.1.1 # Email server -> outside

# Set up DNS
echo "nameserver 8.8.8.8" > /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf

service postfix start 
service dovecot start

# Keep the container running
tail -f /dev/null