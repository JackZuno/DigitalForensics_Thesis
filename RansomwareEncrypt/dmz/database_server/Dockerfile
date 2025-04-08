FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y iputils-ping net-tools iproute2

# Install necessary packages
RUN apt-get update && \
    apt-get install -y traceroute dnsutils

# Update and install iperf
RUN apt-get update && \
    apt-get install -y iperf nano tshark sudo

# Install PostgreSQL and related packages
RUN apt-get install -y postgresql postgresql-contrib

# Clean up
RUN apt-get clean

# Copy the network configuration script
COPY server-config.sh /usr/local/bin/server-config.sh

# Copy the script to create the database and other related stuff
COPY db_setup.sh /usr/local/bin/db_setup.sh

# Make the script executable
RUN chmod +x /usr/local/bin/server-config.sh

# Copy the modified conf files
COPY conf/pg_hba.conf /etc/postgresql/16/main/pg_hba.conf
COPY conf/postgresql.conf /etc/postgresql/16/main/postgresql.conf

# Copy the capture_traffic script and configuration files
COPY pythonScript/capture_traffic.py /usr/local/bin/capture_traffic.py
RUN chmod +x /usr/local/bin/capture_traffic.py

# Create directories for storing captures and logs
RUN mkdir -p /home/captureTraffic

# Run the script and keep the container alive
CMD ["/bin/bash", "-c", "/usr/local/bin/server-config.sh && tail -f /dev/null"]
