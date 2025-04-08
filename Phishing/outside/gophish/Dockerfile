# Dockerfile for GoPhish
FROM gophish/gophish:latest

# Switch to root user
USER root

# Update package list and install necessary packages
RUN apt-get update && apt-get install -y iputils-ping iproute2 net-tools traceroute nano

# Copy the setup script and configuration files
COPY setup.sh /usr/local/bin/setup.sh

# Make sure setup.sh is executable
RUN chmod +x /usr/local/bin/setup.sh

COPY config.json /opt/gophish/config.json

# Run the setup script
CMD ["/bin/bash", "/usr/local/bin/setup.sh"]