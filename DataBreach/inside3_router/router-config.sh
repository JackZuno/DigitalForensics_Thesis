#!/bin/bash

# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Routing
ip route del default via 10.40.0.254
route add default gw 192.168.4.1

ip route add 192.168.1.0/24 via 192.168.4.1 # Servers
ip route add 10.20.0.0/24 via 192.168.4.1 # LAN
ip route add 10.30.0.0/24 via 192.168.4.1 # WLAN

# Set up DNS
echo "nameserver 8.8.8.8" > /etc/resolv.conf

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