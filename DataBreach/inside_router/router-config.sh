#!/bin/bash

# Enable IP forwarding
sysctl -w net.ipv4.ip_forward=1

# Set up DNS
echo "nameserver 8.8.8.8" > /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf

# Routing
ip route del default via 10.20.0.254
route add default gw 192.168.2.1

ip route add 192.168.1.0/24 via 192.168.2.1 # LAN -> Server
ip route add 10.30.0.0/24 via 192.168.2.1 # LAN -> WLAN
ip route add 10.40.0.0/24 via 192.168.2.1 # LAN -> guest

# ip route add 203.0.113.0/24 via 192.168.2.1 # LAN -> Outside

# OSPF Configuration using FRR
cat << EOF > /etc/frr/frr.conf
frr version 7.5
frr defaults traditional
hostname Router
log file /var/log/frr/frr.log
password zebra
router ospf
  network 192.168.2.0/24 area 0
  network 10.20.0.0/24 area 0
EOF

# Start FRR daemons
service frr start
