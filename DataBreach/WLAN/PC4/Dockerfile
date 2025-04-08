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

# Create folder for the content to add into the database
RUN mkdir -p /usr/local/files
COPY files/projectOverview.csv /usr/local/files/projectOverview.csv
COPY files/teamInvolved.csv /usr/local/files/teamInvolved.csv

# Copy the database setup script and configuration files
COPY db_setup.sh /usr/local/bin/db_setup.sh

# Copy the setup script and configuration files
COPY setup.sh /usr/local/bin/setup.sh

# Make the setup script executable
RUN chmod +x /usr/local/bin/setup.sh

# Copy the save_email script and configuration files
COPY pythonScript/save_email.py /usr/local/bin/save_email.py
RUN chmod +x /usr/local/bin/save_email.py

# Create system users with specific UIDs and home directories
RUN adduser --gecos "" --home /home/oliviamurphy oliviamurphy && \
    echo "oliviamurphy:oliviamurphy" | chpasswd && \
    usermod -aG sudo oliviamurphy

# Ensure the sudo group doesn't require a password
RUN echo "oliviamurphy ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

COPY muttrc /home/oliviamurphy/.muttrc

# Ensure correct permissions for the configuration file
RUN chown oliviamurphy:oliviamurphy /home/oliviamurphy/.muttrc

# Create files for store and received emails (with touch they are empty)
RUN touch /home/oliviamurphy/sent
# COPY ./emails/sent /home/oliviamurphy/sent

RUN touch /home/oliviamurphy/inbox

# # Create a profile (If I want it I need to install firefox in a different way)
# RUN mkdir -p /home/oliviamurphy/.mozilla/firefox/profiles
# RUN firefox --headless -CreateProfile "oliviamurphy /home/oliviamurphy/.mozilla/firefox/profiles/oliviamurphy"

# Download folder
RUN mkdir -p /home/oliviamurphy/downloads

# Directory to store files from the database
RUN mkdir -p /home/oliviamurphy/files

COPY certs/.mutt_certificates /home/oliviamurphy/.mutt_certificates

# Run the setup script
CMD ["/bin/bash", "/usr/local/bin/setup.sh"]
