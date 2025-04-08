import imaplib
import email
from email.policy import default

# Configuration
IMAP_SERVER = 'email_server'
IMAP_PORT = 993 # 143
IMAP_USER = 'emilycarter@e-corp.com'
IMAP_PASS = 'emilycarter'
MBOX_FILE = '/home/emilycarter/inbox'  # Updated path

# Connect to the server
try:
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(IMAP_USER, IMAP_PASS)
    mail.select('INBOX')

    # Search for all emails
    result, data = mail.search(None, 'ALL')

    # Create/open mbox file
    with open(MBOX_FILE, 'w') as mbox: # w -> write all file; a -> adding to the existing file
        for num in data[0].split():
            result, msg_data = mail.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1], policy=default)
            mbox.write(f"From {msg['From']} {msg['Date']}\n{msg.as_string()}\n\n")

    # Logout
    mail.logout()
    print(f"Emails saved to {MBOX_FILE}")

except Exception as e:
    print(f"An error occurred: {e}")
