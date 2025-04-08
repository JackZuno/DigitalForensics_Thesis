import time
import re
import subprocess
import imaplib
import email
import os
from email.header import decode_header
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# IMAP server details
IMAP_SERVER = "email_server"  
IMAP_PORT = 993  
USERNAME = "sarahwilliams@e-corp.com"
PASSWORD = "sarahwilliams"  

# Credentials for the phishing landing page
PHISHING_USERNAME = "sarahwilliams"
PHISHING_PASSWORD = "sarah"

profile_path = "/home/sarahwilliams/.mozilla/firefox/profiles/sarahwilliams"
download_dir = "/home/sarahwilliams/downloads"  # Use absolute path

# Set up Firefox options for headless browsing
options = Options()
options.add_argument("--headless")  
options.add_argument("-profile")
options.add_argument(profile_path)

# Setting preferences for downloading files
options.set_preference("browser.download.folderList", 2)  
options.set_preference("browser.download.dir", download_dir)  
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")  
options.set_preference("pdfjs.disabled", True) 

driver = webdriver.Firefox(options=options)

# Connect to the server
def connect_to_email():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT) 
    mail.login(USERNAME, PASSWORD)
    print("Logged in")
    return mail

# Search for phishing emails that match specific criteria
def check_for_phishing_emails(mail):
    mail.select("inbox")
    result, data = mail.search(None, 'ALL')  
    email_ids = data[0].split()

    print("Email found: ", len(email_ids))

    for email_id in email_ids:
        print("Email id: ", email_id)
        result, message_data = mail.fetch(email_id, "(RFC822)")
        for response_part in message_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')

                # Subject
                target_subject = "Scheduled System Maintenance - Verify Your Credentials"

                if target_subject in subject:
                    print(f"New phishing email found: {subject}")
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            if "html" in content_type:
                                body = part.get_payload(decode=True).decode()
                                phishing_url = extract_url(body)
                                return phishing_url
                            elif "plain" in content_type:
                                body = part.get_payload(decode=True).decode()
                    else:
                        # For non-multipart emails
                        body = msg.get_payload(decode=True).decode()
                        phishing_url = extract_url(body)
                        return phishing_url
    print("Nothing found")
    return None

def extract_url(body):
    urls = re.findall(r'http[s]?://[^\s"<>]+', body)

    # Filter out URLs that match known phishing patterns
    for url in urls:
        if '203.0.' in url:
            return url
    return None

# Simulate browser interaction with the phishing page
def open_phishing_url(phishing_url):
    print(f"Opening phishing URL ({phishing_url})")
    driver.get(phishing_url)

    try:
        # Wait for the username field to be present
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        
        # Wait for the password field to be present
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        # Enter credentials
        username_field.send_keys(PHISHING_USERNAME)
        password_field.send_keys(PHISHING_PASSWORD)

        print("Victim got scammed!\n")
        
        # Submit the form
        password_field.submit()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("\nIn the get scammed script\n")
    time.sleep(15)
    mail = connect_to_email()

    while True:
        print("\nLooking for emails...")
        phishing_url = check_for_phishing_emails(mail)
        if phishing_url:
            open_phishing_url(phishing_url)
            break
        time.sleep(45)