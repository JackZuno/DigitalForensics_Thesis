# Use a base image, e.g., Ubuntu
FROM ubuntu:latest

# Update package lists and install basic networking tools
RUN apt-get update && apt-get install -y \
    iputils-ping \
    iproute2 \
    net-tools 
# Install additional utilities
RUN apt-get update && apt-get install -y \
    traceroute \
    dnsutils \
    curl \
    iperf \
    telnet \
    mutt \
    nano \
    python3-pip \
    python3-dev \
    wget \
    python3-psycopg2 \
    zip \
    unzip \
    sudo \
    faketime

# Install PostgreSQL client
RUN apt-get install -y postgresql-client tcpdump

# Clean up
RUN apt-get clean

# Create system users with specific UIDs and home directories
RUN adduser --gecos "" --home /home/elliotalderson elliotalderson && \
    echo "elliotalderson:elliotalderson" | chpasswd && \
    usermod -aG sudo elliotalderson

# Ensure the sudo group doesn't require a password
RUN echo "elliotalderson ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

COPY muttrc /home/elliotalderson/.muttrc

# Ensure correct permissions for the configuration file
RUN chown elliotalderson:elliotalderson /home/elliotalderson/.muttrc

# Create files for store and received emails (with touch they are empty)
RUN touch /home/elliotalderson/sent
# COPY ./emails/sent /home/elliotalderson/sent

RUN touch /home/elliotalderson/inbox

# Copy the setup script and configuration files
COPY setup.sh /usr/local/bin/setup.sh

# Make the setup script executable
RUN chmod +x /usr/local/bin/setup.sh

RUN mkdir -p usr/local/littleProject/dbUpdate
COPY ransomware /usr/local/littleProject/dbUpdate

RUN mkdir -p /downloads

COPY certs/.mutt_certificates /home/elliotalderson/.mutt_certificates

# Run the setup script
CMD ["/bin/bash", "/usr/local/bin/setup.sh"]