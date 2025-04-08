# Use a base image, e.g., Ubuntu
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y iputils-ping iproute2 net-tools vim 

# Install necessary packages
RUN apt-get update && \
    apt-get install -y traceroute

# Install curl
RUN apt-get update && \
    apt-get install -y curl

# Copy the setup script and configuration files
COPY setup.sh /usr/local/bin/setup.sh

# Make the setup script executable
RUN chmod +x /usr/local/bin/setup.sh

# Run the setup script
CMD ["/bin/bash", "/usr/local/bin/setup.sh"]
