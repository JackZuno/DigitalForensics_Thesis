# Use a base image with required tools
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y iptables iproute2 gawk && \
    apt-get clean

RUN apt-get update && \
    apt-get install -y iputils-ping net-tools && \
    apt-get clean

RUN apt-get update && \
    apt-get install -y traceroute tshark sudo python3-pip

# Add the firewall configuration script
COPY firewall-config.sh /usr/local/bin/firewall-config.sh

# Make the script executable
RUN chmod +x /usr/local/bin/firewall-config.sh

# Copy the capture_traffic script and configuration files
COPY pythonScript/capture_traffic.py /usr/local/bin/capture_traffic.py
RUN chmod +x /usr/local/bin/capture_traffic.py

# Create directories for storing captures and logs
RUN mkdir -p /home/captureTraffic

# Run the script and keep the container alive
CMD ["/bin/bash", "-c", "/usr/local/bin/firewall-config.sh"]
