## DayXX (dayXX.py)
This file is the one responsable for sending emails and replying to them, with the ending goal to create a fake conversation.\
In this fil it is possible to send an email or to respond to one. In both cases a fake date and a fake time are used, thanks to the **faketime** command.\
To use a fake date and a fake time with mutt to sending an email I use this command:
```py
# Select the fake date
fake_date = initial_fake_date

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=4, seconds=33))
```
In this case I set **fake_date** equal to **initial_fake_date** (this could be the first email of the day) and then increment the fake time. \
The following step is then calling the function to send the email and passing to it the fake date, that will be used with **faketime** to use mutt with the specific date.

### Send Email
This is an example of how I manage to use the functions that I created to send emails:
```py
# Send email (sarahwilliams -> johndoe)
print("\n---------- Send email (sarahwilliams -> johndoe) ----------")

# Set the email arguments
email_subject = "Weekly Project Update"
email_body = (
    "Hi John,\n\n"
    "I hope you are doing well. Just wanted to touch base regarding our current project milestones.\n"
    "Could we schedule a quick meeting tomorrow morning to discuss the latest developments and address any pending tasks?\n\n"
    "Looking forward to your response.\n\n"
    "Best,\nSarah\n"
)

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=3, minutes=12, seconds=43))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = johndoe_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)
```
### Reply Email
In case of the response, before answering to the email, I call the function **save_email** on the container of the one that will respond to the email. I do that so the inbox file will be updated with the latest email received in order to be able to respond to the selected email.\
This is an example of how I manage to use the functions that I created to reply to emails:
```py
# Reply email (johndoe -> sarahwilliams)
print("\n---------- Reply email (johndoe -> sarahwilliams) ----------")

# Retrieve the email with johndoe
save_email(johndoe_computer2)

# Set the email arguments
email_subject = "Re: Weekly Project Update"
email_body = (
    "Hi Sarah,\n\n"
    "Sorry for the late response.\n"
    "Yes, I do not have much time but we can do it today in the afternoon.\n\n"
    "Best regards,\nJohn\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=4, seconds=4))

# Set the parameter for the functions
container = johndoe_computer2
receiver = sarahwilliams_email
sender = "johndoe"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)
```

### Ransomware Attack
#### Attacker Side: Zip Folder
In this part of the script the attacker zip the folder containing the fake update to send to the victims. The operations are executed under a fake date.
```py
# Zip the ransomware and then send it via email
print("\n---------- ZIP the ransomware folder ----------")

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=44, seconds=23))

container = elliotalderson_attacker

# Set the fake date and time and then zip the file
set_fake_time(container, fake_date)
zip_ransomware_folder(container)

time.sleep(10)
```

#### Attacker Side: Send The Email
In this part the attacker send the email to different persons with the zipped folder attached.
```py
# Send it via email
print("\n---------- Send ransomware via email (elliotalderson -> sarahwilliams, sampointer, emilycarter) ----------")

# Set the email arguments
email_subject = "Important Security Update: Action Required"
email_body = (
    "Dear Team,\n"
    "We are reaching out to inform you of an important security update that is now available.\n"
    "This update includes security improvements and enhances the overall performance of the application.\n"
    "Please install this update as soon as possible to keep your software secure and up to date.\n\n"
    "To install the update, please follow these steps:\n"
    "1. Download the attached ZIP file to your device.\n"
    "2. Extract the contents of the ZIP file.\n"
    "3. Open the folder and follow the instructions provided in the \"ReadMe\" file to complete the installation.\n\n"
    "If you have any questions or need assistance, please contact our support team at support@e-corp.com.\n\n"
    "Best regards,\nThe IT E-Corp Team\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=56, seconds=3))

# Set the parameter for the functions
container = elliotalderson_attacker
receiver = f"{sarahwilliams_email} {sampointer_email} {emilycarter_email} {oliviamurphy_email}"
sender = "elliotalderson"

# Attachment
attachment_path = "/usr/local/littleProject/dbUpdate.zip"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_with_attach(container, fake_date, receiver, email_subject, email_body, sender, attachment_path)

# Sleep
time.sleep(5)
```

#### Victim Side: Save the Attachment
In this part the victim extract from the email the attachment.
```py
# Save attachment
print("\n---------- Save the zipped ransomware folder ----------")

container = sarahwilliams_computer1
user = "sarahwilliams"  

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=3, minutes=27, seconds=35))

set_fake_time(container, fake_date)
save_attachment_from_email(container, user)

time.sleep(5)
```

#### Victim Side: Unzip the Folder
In this part the victim unzip the folder that was attached into the email.
```py
# Unzip folder
print("\n---------- Unzip the zipped ransomware folder ----------")

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=10, seconds=21))

container = sarahwilliams_computer1
user = "sarahwilliams"
folder_zip_name = "dbUpdate.zip"
target_zip = f"/home/{user}/downloads/{folder_zip_name}"
working_dir = f"/home/{user}"

set_fake_time(container, fake_date)
unzip_ransomware_folder(container, fake_date, user, target_zip, working_dir)
```

#### Victim Side: Run the Malicious Script
In this part the victim run the **installer.py**.
```py
# Install the update
print("\n---------- Install the ransomware update ----------")

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=6, seconds=26))

container = sarahwilliams_computer1
user = "sarahwilliams"

set_fake_time(container, fake_date)
run_ransomware_script(container, user)

time.sleep(10)
```
