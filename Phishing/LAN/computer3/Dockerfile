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

# Allow tshark to capture network packets without root privileges
RUN setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap

# Download geckodriver binary
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz

# Extract the binary
RUN tar -xzvf geckodriver-v0.35.0-linux64.tar.gz
RUN rm geckodriver-v0.35.0-linux64.tar.gz

# Move the binary to /usr/local/bin/
RUN mv geckodriver /usr/local/bin/

# Download and extract Firefox
RUN wget -O /tmp/firefox.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"
RUN tar -xjf /tmp/firefox.tar.bz2 -C /opt/
RUN ln -s /opt/firefox/firefox /usr/local/bin/
RUN rm /tmp/firefox.tar.bz2

# Install Selenium
RUN pip3 install selenium

# Copy the setup script and configuration files
COPY setup.sh /usr/local/bin/setup.sh

# Make the setup script executable
RUN chmod +x /usr/local/bin/setup.sh

# Copy the save_email script and configuration files
COPY pythonScript/save_email.py /usr/local/bin/save_email.py
RUN chmod +x /usr/local/bin/save_email.py

# Other python script
COPY pythonScript/get_scammed.py /usr/local/bin/get_scammed.py

# Create system users with specific UIDs and home directories
RUN adduser --gecos "" --home /home/emilycarter emilycarter && \
    echo "emilycarter:emilycarter" | chpasswd && \
    usermod -aG sudo emilycarter

# Ensure the sudo group doesn't require a password
RUN echo "emilycarter ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

COPY muttrc /home/emilycarter/.muttrc

# Ensure correct permissions for the configuration file
RUN chown emilycarter:emilycarter /home/emilycarter/.muttrc

# Create files for store and received emails (with touch they are empty)
RUN touch /home/emilycarter/sent
# COPY ./emails/sent /home/emilycarter/sent

RUN touch /home/emilycarter/inbox

# Create a profile (If I want it I need to install firefox in a different way)
RUN mkdir -p /home/emilycarter/.mozilla/firefox/profiles
RUN firefox --headless -CreateProfile "emilycarter /home/emilycarter/.mozilla/firefox/profiles/emilycarter"

# Download folder
RUN mkdir -p /home/emilycarter/downloads

# Directory to store files from the database
RUN mkdir -p /home/emilycarter/files

COPY certs/.mutt_certificates /home/emilycarter/.mutt_certificates

# Run the setup script
CMD ["/bin/bash", "/usr/local/bin/setup.sh"]
