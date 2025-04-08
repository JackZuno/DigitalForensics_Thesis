# Use a base image, e.g., Ubuntu
FROM ubuntu:22.04

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

# # Create a profile (If I want it I need to install firefox in a different way)
# RUN mkdir -p /home/elliotalderson/.mozilla/firefox/profiles
# RUN firefox --headless -CreateProfile "elliotalderson /home/elliotalderson/.mozilla/firefox/profiles/elliotalderson"

# Download folder
RUN mkdir -p /home/elliotalderson/downloads

# Directory to store files from the database
RUN mkdir -p /home/elliotalderson/files

COPY certs/.mutt_certificates /home/elliotalderson/.mutt_certificates

# Run the setup script
CMD ["/bin/bash", "/usr/local/bin/setup.sh"]