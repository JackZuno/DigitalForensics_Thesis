import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 12 ##########################

print("\n-------------- DAY 12 (Data Breach) --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=11, minutes=12, seconds=22))

print("Starting date DAY 12: ", fake_date, "\n")

###########################################################
# Send email (sampointer -> sarahwilliams)
print("\n---------- Send email (sampointer -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Meeting Room Setup for Presentation"
email_body = (
    "Hi Sarah,\n"
    "I saw that you have got a presentation next week in the main conference room.\n"
    "Do you need any special setup for your equipment, or will the standard setup work?\n\n"
    "Best,\nSam\n"
)

# Set the parameter for the functions
container = sampointer_pc1
receiver = sarahwilliams_email
sender = "sampointer"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
# Reply email (sarahwilliams -> emilycarter)
print("\n---------- Reply email (sarahwilliams -> emilycarter) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Resource Allocation for Next Quarter"
email_body = (
    "Hi Emily,\n\n"
    "Lets aim for Thursday afternoon to review the resource allocation.\n"
    "I will pull together some preliminary data so we can make informed decisions.\n\n"
    "Thanks for flagging this!\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=13, seconds=19))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = emilycarter_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Reply email (sarahwilliams -> sampointer)
print("\n---------- Reply email (sarahwilliams -> sampointer) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Meeting Room Setup for Presentation"
email_body = (
    "Hi Sam,\n\n"
    "The standard setup should work just fine.\n"
    "I will let you know if anything changes, but as of now, I think we are all set.\n\n"
    "Thanks for checking in!\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=2, minutes=55, seconds=39))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = sampointer_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)
