import imaplib
import email
import os

# Configuration
IMAP_SERVER = 'email_server'
EMAIL_ACCOUNT = 'sarahwilliams@e-corp.com'   
EMAIL_PASSWORD = 'sarahwilliams'          
SUBJECT = "Important Security Update: Action Required"  
SAVE_DIR = os.path.expanduser("/home/sarahwilliams/downloads") 

os.makedirs(SAVE_DIR, exist_ok=True)

def save_attachment(part):
    filename = part.get_filename()
    if filename:
        file_path = os.path.join(SAVE_DIR, filename)
        with open(file_path, 'wb') as f:
            f.write(part.get_payload(decode=True))
        print(f"Saved attachment: {file_path}")

def main():
    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)

    # Select the mailbox you want to search
    mail.select("inbox")

    # Search for emails by subject
    result, data = mail.search(None, f'SUBJECT "{SUBJECT}"')

    if result == "OK":
        for num in data[0].split():
            # Fetch the email by ID
            result, msg_data = mail.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])

            # Iterate through email parts to find attachments
            for part in msg.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                save_attachment(part)
    else:
        print("No emails found.")

    mail.logout()

if __name__ == "__main__":
    main()