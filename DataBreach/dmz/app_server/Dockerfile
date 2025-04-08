FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y iputils-ping net-tools iproute2

# Install necessary packages
RUN apt-get update && \
    apt-get install -y traceroute

# Update and install iperf
RUN apt-get update && \
    apt-get install -y iperf

# Copy the network configuration script
COPY server-config.sh /usr/local/bin/server-config.sh

# Make the script executable
RUN chmod +x /usr/local/bin/server-config.sh

# Run the script and keep the container alive
CMD ["/bin/bash", "-c", "/usr/local/bin/server-config.sh && tail -f /dev/null"]
