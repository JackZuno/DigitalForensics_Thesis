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
COPY files/keyMeasurements.csv /usr/local/files/keyMeasurements.csv
COPY files/locations.csv /usr/local/files/locations.csv

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
RUN adduser --gecos "" --home /home/annamoore annamoore && \
    echo "annamoore:annamoore" | chpasswd && \
    usermod -aG sudo annamoore

# Ensure the sudo group doesn't require a password
RUN echo "annamoore ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

COPY muttrc /home/annamoore/.muttrc

# Ensure correct permissions for the configuration file
RUN chown annamoore:annamoore /home/annamoore/.muttrc

# Create files for store and received emails (with touch they are empty)
RUN touch /home/annamoore/sent
COPY ./emails/sent /home/annamoore/sent

RUN touch /home/annamoore/inbox

# # Create a profile (If I want it I need to install firefox in a different way)
# RUN mkdir -p /home/annamoore/.mozilla/firefox/profiles
# RUN firefox --headless -CreateProfile "annamoore /home/annamoore/.mozilla/firefox/profiles/annamoore"

# Download folder
RUN mkdir -p /home/annamoore/downloads

# Directory to store files from the database
RUN mkdir -p /home/annamoore/files

COPY certs/.mutt_certificates /home/annamoore/.mutt_certificates

# Run the setup script
CMD ["/bin/bash", "/usr/local/bin/setup.sh"]
