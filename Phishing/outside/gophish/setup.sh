#!/bin/bash

# Modify routing settings
ip route del default via 203.0.113.254
route add default gw 203.0.113.1

ip route add 10.20.0.0/24 via 203.0.113.1

# hostname resolution
echo "192.168.1.4 email_server" >> /etc/hosts

# Start GoPhish server
exec ./gophish