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
