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
    python3-psycopg2 \
    zip \
    unzip

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
    sudo \
    faketime

# Install audio and graphics libraries
RUN apt-get update && apt-get install -y \
    libasound2 \
    libgl1-mesa-glx 

# Install PostgreSQL client
RUN apt-get install -y postgresql-client

# Install tool to run script periodically
RUN apt-get update && apt-get install -y cron sqlite3

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

# Install pandas (merge files)
RUN pip3 install pandas

# Copy the setup script and configuration files
COPY setup.sh /usr/local/bin/setup.sh

# Make the setup script executable
RUN chmod +x /usr/local/bin/setup.sh

# Copy the script with the fake bash history
COPY fake_history.sh /usr/local/bin/fake_history.sh

# Copy your Python script
COPY pythonScript/query.py /usr/local/bin/query.py
COPY pythonScript/get_scammed.py /usr/local/bin/get_scammed.py
COPY pythonScript/capture_traffic.py /usr/local/bin/capture_traffic.py
COPY pythonScript/capture_phishing.py /usr/local/bin/capture_phishing.py
COPY pythonScript/web_nav/start_web_nav.py /usr/local/bin/start_web_nav.py

# Copy the save_email script and configuration files
COPY pythonScript/save_email.py /usr/local/bin/save_email.py
RUN chmod +x /usr/local/bin/save_email.py

# Create system users with specific UIDs and home directories
RUN adduser --gecos "" --home /home/sarahwilliams sarahwilliams && \
    echo "sarahwilliams:sarahwilliams" | chpasswd && \
    usermod -aG sudo sarahwilliams

# Ensure the sudo group doesn't require a password
RUN echo "sarahwilliams ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

COPY muttrc /home/sarahwilliams/.muttrc

# Ensure correct permissions for the configuration file
RUN chown sarahwilliams:sarahwilliams /home/sarahwilliams/.muttrc

# Create files for store and received emails (with touch they are empty)
RUN touch /home/sarahwilliams/sent
# COPY ./emails/sent /home/sarahwilliams/sent

RUN touch /home/sarahwilliams/inbox

# Create a profile
RUN mkdir -p /home/sarahwilliams/.mozilla/firefox/profiles
RUN firefox --headless -CreateProfile "SarahWilliams /home/sarahwilliams/.mozilla/firefox/profiles/sarahwilliams"

# Download folder
RUN mkdir -p /home/sarahwilliams/downloads

# Directory to store files from the database
RUN mkdir -p /home/sarahwilliams/files

# Directory with files that will be encrypted/stolen
RUN mkdir -p /home/sarahwilliams/new_ideas/info

# Create directories for storing captures and logs
RUN mkdir -p /home/sarahwilliams/networkCapture
RUN mkdir -p /home/sarahwilliams/networkCapture/web_navigation
RUN mkdir -p /home/sarahwilliams/networkCapture/email_and_db
RUN mkdir -p /home/sarahwilliams/networkCapture/phishing

RUN touch /home/sarahwilliams/networkCapture/keylogfile.txt

# Set the SSLKEYLOGFILE environment variable for capturing TLS keys
RUN echo "export SSLKEYLOGFILE=/home/sarahwilliams/networkCapture/keylogfile.txt" >> /home/sarahwilliams/.bashrc

COPY certs/.mutt_certificates /home/sarahwilliams/.mutt_certificates

# Run the setup script
# CMD ["/bin/bash", "/usr/local/bin/setup.sh"]
CMD ["/bin/bash", "-c", "/usr/local/bin/setup.sh && tail -f /dev/null"]