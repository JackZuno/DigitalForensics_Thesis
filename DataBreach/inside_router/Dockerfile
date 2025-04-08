FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y iputils-ping net-tools iproute2 frr && \
    apt-get clean

# Install necessary packages
RUN apt-get update && \
    apt-get install -y traceroute dnsutils curl iperf

# Copy the network configuration script
COPY router-config.sh /usr/local/bin/router-config.sh

# Make the script executable
RUN chmod +x /usr/local/bin/router-config.sh

CMD ["/bin/bash", "-c", "/usr/local/bin/router-config.sh && tail -f /dev/null"]
