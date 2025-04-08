#!/bin/bash

# Set up DNS
echo "nameserver 8.8.8.8" > /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf

# Enable IP forwarding
sysctl -w net.ipv4.ip_forward=1

# Routing
ip route del default via 203.0.113.254
route add default gw 203.0.114.254

ip route add 192.168.1.0/24 via 198.51.100.1 # Outside -> Server
ip route add 10.20.0.0/24 via 198.51.100.1 # Outside -> LAN
ip route add 10.30.0.0/24 via 198.51.100.1 # Outside -> WLAN
ip route add 10.40.0.0/24 via 198.51.100.1 # Outside -> guest

# These are needed to keep the NAT working
INTERNET_IFACE=$(sh -c "ip -o -4 addr show | grep '203.0.114.1' | cut -d' ' -f2")
echo "The inernet interface is $INTERNET_IFACE"

iptables -t nat -A POSTROUTING -o "$INTERNET_IFACE" -j MASQUERADE
