# Use a base image, e.g., Ubuntu
FROM ubuntu:22.04

# ubuntu:22.04  instead of unbuntu:latest because libasound2 and libgl1-mesa-glx are not available

# Set the frontend to noninteractive to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

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
    mailutils \
    telnet \
    mutt \
    nano \
    python3-pip \
    python3-dev \
    wget \
    zip \
    unzip \
    sudo \
    faketime

# Install GUI-related libraries
RUN apt-get update && apt-get install -y \
    firefox \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libx11-xcb1 \
    libxt6 \
    libxrender1 \
    libxcomposite1 \
    libpangocairo-1.0-0 \
    libvulkan1 \
    tshark \
    wget \
    python3-psycopg2

# Install audio and graphics libraries
RUN apt-get update && apt-get install -y \
    libasound2 \
    libgl1-mesa-glx 

# Install PostgreSQL client
RUN apt-get install -y postgresql-client

# Install tool to run script periodically
RUN apt-get update && apt-get install -y cron sqlite

# Clean up
RUN apt-get clean

# Copy the setup script and configuration files
COPY setup.sh /usr/local/bin/setup.sh

# Make the setup script executable
RUN chmod +x /usr/local/bin/setup.sh

# Copy the save_email script and configuration files
COPY pythonScript/save_email.py /usr/local/bin/save_email.py

# Create system users with specific UIDs and home directories
RUN adduser --gecos "" --home /home/johndoe johndoe && \
    echo "johndoe:johndoe" | chpasswd && \
    usermod -aG sudo johndoe

# Ensure the sudo group doesn't require a password
RUN echo "johndoe ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

COPY muttrc /home/johndoe/.muttrc

# Ensure correct permissions for the configuration file
RUN chown johndoe:johndoe /home/johndoe/.muttrc

# Create files for store and received emails (with touch they are empty)
RUN touch /home/johndoe/sent
COPY ./emails/sent /home/johndoe/sent

RUN touch /home/johndoe/inbox

# # Create a profile (If I want it I need to install firefox in a different way)
# RUN mkdir -p /home/johndoe/.mozilla/firefox/profiles
# RUN firefox --headless -CreateProfile "johndoe /home/johndoe/.mozilla/firefox/profiles/johndoe"

# Download folder
RUN mkdir -p /home/johndoe/downloads

# Directory to store files from the database
RUN mkdir -p /home/johndoe/files

COPY certs/.mutt_certificates /home/johndoe/.mutt_certificates

# Run the setup script
CMD ["/bin/bash", "/usr/local/bin/setup.sh"]
