#!/bin/bash

# Enable IP forwarding
sysctl -w net.ipv4.ip_forward=1

echo "nameserver 8.8.8.8" > /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf

# Routing
ip route del default via 192.168.1.254
route add default gw 198.51.101.254

ip route add 10.20.0.0/24 via 192.168.2.2 # firewall -> LAN
ip route add 10.30.0.0/24 via 192.168.3.2 # firewall -> WLAN
ip route add 10.40.0.0/24 via 192.168.4.2 # firewall -> guest

ip route add 203.0.113.0/24 via 198.51.100.2 # firewall -> outside    # line added to route to the outside

# These are needed to keep the NAT working after the change of the gateway
OUTSIDE_NET_IFACE=$(sh -c "ip -o -4 addr show | grep '198.51.100.1' | cut -d' ' -f2")
echo "The outside_net interface is $OUTSIDE_NET_IFACE"

EXT_NET_IFACE=$(sh -c "ip -o -4 addr show | grep '198.51.101.1' | cut -d' ' -f2")
echo "The external_net interface is $EXT_NET_IFACE"

iptables -t nat -A POSTROUTING -o "$OUTSIDE_NET_IFACE" -j MASQUERADE
iptables -t nat -A POSTROUTING -o "$EXT_NET_IFACE" -j MASQUERADE

# Block traffic from 10.40.0.0/24 to 10.20.0.0/24 unless part of an established connection
iptables -A FORWARD -s 10.40.0.0/24 -d 10.20.0.0/24 -m state ! --state ESTABLISHED,RELATED -j DROP

# Block traffic from 10.40.0.0/24 to 10.30.0.0/24 unless part of an established connection
iptables -A FORWARD -s 10.40.0.0/24 -d 10.30.0.0/24 -m state ! --state ESTABLISHED,RELATED -j DROP

# Allow return traffic (part of or related to established connections)
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow traffic from 10.20.0.0/24 and 10.30.0.0/24 to other destinations
iptables -A FORWARD -s 10.20.0.0/24 -j ACCEPT
iptables -A FORWARD -s 10.30.0.0/24 -j ACCEPT

# Allow traffic from 10.40.0.0/24 to other destinations
iptables -A FORWARD -s 10.40.0.0/24 -j ACCEPT

# Allow traffic from outside to DMZ
iptables -A FORWARD -i $OUTSIDE_NET_IFACE -o dmz_net -d 192.168.1.0/24 -j ACCEPT

# Allow traffic from dmz to outside
iptables -A FORWARD -s 192.168.1.0/24 -o $EXT_NET_IFACE -j ACCEPT

# Allow traffic from outside to dmz (New line added to allow the attacker to ping the dmz)
iptables -A FORWARD -s 198.51.100.0/24 -d 192.168.1.0/24 -j ACCEPT
iptables -A FORWARD -s 203.0.113.0/24 -d 192.168.1.0/24 -j ACCEPT
iptables -A FORWARD -s 192.168.1.0/24 -d 203.0.113.0/24 -j ACCEPT   # line added to allow the dmz to ping the outside
iptables -A FORWARD -s 192.168.1.0/24 -d 198.51.100.0/24 -j ACCEPT   # line added to allow the dmz to ping the outside

# Deny traffic from outside to internal networks
iptables -A FORWARD -i $OUTSIDE_NET_IFACE -o inside1_net -d 10.20.0.0/24 -j DROP
iptables -A FORWARD -i $OUTSIDE_NET_IFACE -o inside2_net -d 10.30.0.0/24 -j DROP
iptables -A FORWARD -i $OUTSIDE_NET_IFACE -o inside3_net -d 10.40.0.0/24 -j DROP

# Allow established and related traffic
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow traffic from internal networks to outside
iptables -A FORWARD -i inside1_net -o $OUTSIDE_NET_IFACE -j ACCEPT
iptables -A FORWARD -i inside2_net -o $OUTSIDE_NET_IFACE -j ACCEPT
iptables -A FORWARD -i inside3_net -o $OUTSIDE_NET_IFACE -j ACCEPT

# Allow traffic from DMZ to Inside1 (10.20.0.0/24)
iptables -A FORWARD -s 192.168.1.0/24 -d 10.20.0.0/24 -j ACCEPT

# Allow traffic from DMZ to Inside2 (10.30.0.0/24)
iptables -A FORWARD -s 192.168.1.0/24 -d 10.30.0.0/24 -j ACCEPT

# Allow traffic from DMZ to Inside3 (10.40.0.0/24)
iptables -A FORWARD -s 192.168.1.0/24 -d 10.40.0.0/24 -j ACCEPT

# Set default policy to drop for the FORWARD chain
iptables -P FORWARD DROP

# Keep the container running
tail -f /dev/null
