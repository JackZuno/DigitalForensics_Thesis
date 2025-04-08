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
RUN apt-get install -y postgresql-client

# Install tool to run script periodically
RUN apt-get update && apt-get install -y cron

# Clean up
RUN apt-get clean

# Copy the setup script and configuration files
COPY setup.sh /usr/local/bin/setup.sh

# Make the setup script executable
RUN chmod +x /usr/local/bin/setup.sh

# Copy the save_email script and configuration files
COPY pythonScript/save_email.py /usr/local/bin/save_email.py
RUN chmod +x /usr/local/bin/save_email.py

# Copy python script to retrieve info to file
COPY script/query.py /usr/local/bin/query.py

# Create system users with specific UIDs and home directories
RUN adduser --gecos "" --home /home/jakethompson jakethompson && \
    echo "jakethompson:jakethompson" | chpasswd && \
    usermod -aG sudo jakethompson

# Ensure the sudo group doesn't require a password
RUN echo "jakethompson ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

COPY muttrc /home/jakethompson/.muttrc

# Ensure correct permissions for the configuration file
RUN chown jakethompson:jakethompson /home/jakethompson/.muttrc

# Create files for store and received emails (with touch they are empty)
RUN touch /home/jakethompson/sent
COPY ./emails/sent /home/jakethompson/sent

RUN touch /home/jakethompson/inbox

# # Create a profile (If I want it I need to install firefox in a different way)
# RUN mkdir -p /home/jakethompson/.mozilla/firefox/profiles
# RUN firefox --headless -CreateProfile "jakethompson /home/jakethompson/.mozilla/firefox/profiles/jakethompson"

# Download folder
RUN mkdir -p /home/jakethompson/downloads

# Directory to store files from the database
RUN mkdir -p /home/jakethompson/files

COPY certs/.mutt_certificates /home/jakethompson/.mutt_certificates

# Run the setup script
CMD ["/bin/bash", "/usr/local/bin/setup.sh"]
