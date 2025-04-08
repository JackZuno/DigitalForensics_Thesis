## Problems
### Email Server
#### Authentication
When I was dealing with the authenticaction setup with Dovecot, I had problems to perfrom the login, because it wasn't able to find the user. \
The problem was how I was storing the data about the user.\
Wrong way:
```Dockerfile
# Create a user database file for Dovecot
RUN echo "sarahwilliams@e-corp.com:sarahwilliams" >> /etc/dovecot/users && \
    echo "johndoe@e-corp.com:johndoe" >> /etc/dovecot/users
```
Right way:
```Dockerfile
# Dynamically get the uid and gid for sarahwilliams and johndoe
RUN uid1=$(id -u sarahwilliams) && gid1=$(id -g sarahwilliams) && \
    uid2=$(id -u johndoe) && gid2=$(id -g johndoe) && \
    echo "sarahwilliams:{PLAIN}sarahwilliams:${uid1}:${gid1}::/home/sarahwilliams:/bin/false" >> /etc/dovecot/users && \
    echo "johndoe:{PLAIN}johndoe:${uid2}:${gid2}::/home/johndoe:/bin/false" >> /etc/dovecot/users
```

#### Ports
Depending on with protocol is used, the right ports must be exposed and used. \
For IMAP, if you want to use SSL/TLS you need to use port **993**, if not port **143**. \
For SMTP, for sending emails in plain you can use port **25**, if you want to use STARTTLS you can use port **587**, and, in the end, if you wand to use SSL/TLS from the start you need to use port **465** (now deprecated). 

### Firefox
#### Ubuntu Version Packages
I didn't use "ubuntu:latest" because there were problems with the packages needed for firefox.
```Dockerfile
FROM ubuntu:22.04
```
Packages needed for firefox:
```Dockerfile
# Install GUI-related libraries
RUN apt-get update && apt-get install -y \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libx11-xcb1 \
    libxt6 \
    libxrender1 \
    libxcomposite1 \
    libpangocairo-1.0-0 \
    libvulkan1
```
Packages that create problems with ubuntu:latest but not with ubuntu:22.04:
```Dockerfile
# Install audio and graphics libraries
RUN apt-get update && apt-get install -y \
    libasound2 \
    libgl1-mesa-glx
```

#### Firefox Installation
I had problems with the installation of firefox with apt-get:
```Dockerfile
RUN apt-get update && apt-get install -y firefox
```
The problem is that when I was trying to create a profile in firefox with
``` Dockerfile
# Create a profile
RUN mkdir -p /home/sarahwilliams/.mozilla/firefox/profiles
RUN firefox --headless -CreateProfile "SarahWilliams /home/sarahwilliams/.mozilla/firefox/profiles/sarahwilliams"
```
I had errors that refer to snapd asking me to install firefox snap:
```bash
# Command
firefox --version

# Error
Command '/usr/bin/firefox' requires the firefox snap to be installed.
Please install it with:
snap install firefox
```
After trying to run *snap install firefox* nothing worked. \
To solve this problem I changed the method for the installation and I used **wget**:
```Dockerfile
# Download and extract Firefox
RUN wget -O /tmp/firefox.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"
RUN tar -xjf /tmp/firefox.tar.bz2 -C /opt/
RUN ln -s /opt/firefox/firefox /usr/local/bin/
RUN rm /tmp/firefox.tar.bz2
```

#### GeckoDriver
Selenium Firefox Driver, also called GeckoDriver, is a browser rendering engine developed by Mozilla for many applications. It provides a link between test cases and the Firefox browser. Without the help of GeckoDriver, one cannot instantiate the object of the Firefox browser and perform automated Selenium testing.
Mozila Firefox requires GeckoDriver because from version 47.x onwards it comes with Marionette, which is an automation driver for Mozilla's Gecko engine. It can remotely control either the UI or the internal JavaScript of a Gecko platform, such as Firefox.
```Dockerfile
# Download geckodriver binary
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz

# Extract the binary
RUN tar -xzvf geckodriver-v0.35.0-linux64.tar.gz
RUN rm geckodriver-v0.35.0-linux64.tar.gz

# Move the binary to /usr/local/bin/
RUN mv geckodriver /usr/local/bin/
```

### Dockerfile Commands
#### Non Interactive
Due to the fact that there is no GUI access and this phase must be automatic, in the Dockerfile you need to deal with the installation of packages that requires the interaction of the user. For example, sometimes they ask you a question that can be answered with Yes[Y] or No[N], and it must be answered in order to continue the installation.
```Dockerfile
# Set the frontend to noninteractive to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive
```

#### Wireshark
In this case I use tshark (the wireshark version for command line) and to make it works it needs permissions to capture the traffic.
```Dockerfile
# Allow tshark to capture network packets without root privileges
RUN setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap
```

### Browsing With Selenium
#### Settings
It is important to add this argument to options, because with selenium, in this case, there is no access to the GUI so in headless mode it is possible to navigate.
```py
options.add_argument("--headless") 
```
The full configuration of the firefox options are:
```py
profile_path = "/home/sarahwilliams/.mozilla/firefox/profiles/sarahwilliams"
download_dir = "/home/sarahwilliams/downloads"

# Set up Firefox options
options = Options()
options.add_argument("--headless")  # Needed because there is no UI
options.add_argument("-profile")
options.add_argument(profile_path)

# Setting preferences for downloading files
options.set_preference("browser.download.folderList", 2)  # Use custom download directory
options.set_preference("browser.download.dir", download_dir)  # Set download directory
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")  # Auto-download PDF
options.set_preference("pdfjs.disabled", True)  # Disable built-in PDF viewer
```
In this case I set a download directory to store the dowloaded files and I add the settings that allow me to download PDFs without accessing the GUI.

#### Cookies
When navigating on internet with selenium, you must be careful to deal with the cookies. In this case, when I am trying to open google.com and then search something, before the search there are the cookies that must be accepted (or refused). \
I made a function to accept, if requested, the cookies trying different languages:
```py
def accept_cookies(driver):
    # List of possible translations for the cookie acceptance button
    cookie_acceptance_texts = [
        "Accetta tutto",  # Italian
        "Accept all",     # English
        "Aceptar todo",   # Spanish
        "Accepter tout",  # French
        "Alle akzeptieren", # German
        "Akceptuj wszystkie", # Polish
        "Aceitar todos",  # Portuguese
        "Aceptar todas"   # Latin American Spanish
    ]
    
    cookie_accepted = False  # Flag to check if cookies were accepted

    for text in cookie_acceptance_texts:
        try:
            # Wait for the cookie acceptance button to be present
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//div[text()='{text}']"))
            )
            # Try to find the cookie acceptance button
            agree_button = driver.find_element(By.XPATH, f"//div[text()='{text}']")
            if agree_button.is_displayed():
                agree_button.click()
                print(f"Accepted cookies with text: '{text}'")
                cookie_accepted = True
                break  # Exit the loop if cookies were accepted
        except Exception:
            continue  # Continue to the next translation if the current one fails

    if not cookie_accepted:
        print("Cookie acceptance not required or failed in all languages.")
```
