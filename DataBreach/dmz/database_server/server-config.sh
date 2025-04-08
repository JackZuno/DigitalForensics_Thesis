#!/bin/bash

# Set up DNS
echo "nameserver 8.8.8.8" > /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf

# Routing
ip route del default via 192.168.1.254
route add default gw 192.168.1.1

ip route add 10.20.0.0/24 via 192.168.1.1   # DB server -> LAN
ip route add 192.168.2.0/24 via 192.168.1.1 # DB server -> inside_router
ip route add 10.30.0.0/24 via 192.168.1.1   # DB server -> WLAN
ip route add 10.40.0.0/24 via 192.168.1.1   # DB server -> guest

ip route add 198.51.100.0/24 via 192.168.1.1 # DB server -> outside

# Initialize PostgreSQL data directory (this happens on first run)
PGDATA="/var/lib/postgresql/data"
if [ ! -d "$PGDATA" ]; then
    echo "Initializing PostgreSQL data directory..."
    su - postgres -c "/usr/lib/postgresql/$(pg_lsclusters -h | awk '{print $1}')/bin/initdb -D $PGDATA"
fi

# Start PostgreSQL service
service postgresql start

# Configure PostgreSQL: Create a user, database, and set permissions
echo "Setting up PostgreSQL user, database, and permissions..."

# Script to setup the Database
source /usr/local/bin/db_setup.sh

echo "PostgreSQL setup completed!"

# Keep the container running
# tail -f /dev/null