#!/bin/bash

# Set up resolv.conf
echo "nameserver 8.8.8.8" > /etc/resolv.conf

# Routing
ip route del default via 10.40.0.254
route add default gw 10.40.0.253

ip route add 192.168.1.0/24 via 10.40.0.253
ip route add 10.20.0.0/24 via 10.40.0.253 
ip route add 10.30.0.0/24 via 10.40.0.253 

# Keep the container running
tail -f /dev/null
