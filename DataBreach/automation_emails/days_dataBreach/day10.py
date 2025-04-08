import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 10 ##########################

print("\n-------------- DAY 10 (Data Breach) --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=9, minutes=2, seconds=45))

print("Starting date DAY 10: ", fake_date, "\n")

###########################################################
# Send email (sarahwilliams -> elliotalderson)
print("\n---------- Send email (sarahwilliams -> elliotalderson) ----------")

# Set the email arguments
email_subject = "Follow-Up on Files"
email_body = (
    "Hi Elliot,\n"
    "Did you get a chance to look over the files?\n"
    "I think we need to strategize our next steps now that we have the information.\n\n"
    "Let me know when you are free to discuss.\n\n"
    "Best,\nSarah\n"
)

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = elliotalderson_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
# Send email (oliviamurphy -> sarahwilliams)
print("\n---------- Send email (oliviamurphy -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Reminder: Client Call at 3 PM"
email_body = (
    "Hi Sarah,\n"
    "Just a quick reminder that we have the call with the client at 3 PM today.\n"
    "I will dial in a few minutes early to make sure everything is set up.\n"
    "Lets try to address their questions about the recent changes to the project scope.\n\n"
    "Talk to you soon,\nOlivia\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=46, seconds=23))

# Set the parameter for the functions
container = oliviamurphy_pc4
receiver = sarahwilliams_email
sender = "oliviamurphy"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
# Reply email (elliotalderson -> sarahwilliams)
print("\n---------- Reply email (elliotalderson -> sarahwilliams) ----------")

# Retrieve the email with elliotalderson
save_email(elliotalderson_attacker)

# Set the email arguments
email_subject = "Re: Follow-Up on Files"
email_body = (
    "Hi Sarah,\n\n"
    "I reviewed the files, and everything looks good.\n"
    "The data is solid, and I think we are ready to move forward.\n"
    "We should set up a time to finalize our strategy.\n\n"
    "Lets aim for next week. How does Tuesday sound?\n\n"
    "Best,\nElliot\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=35, seconds=22))

# Set the parameter for the functions
container = elliotalderson_attacker
receiver = sarahwilliams_email
sender = "elliotalderson"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Reply email (sarahwilliams -> oliviamurphy)
print("\n---------- Reply email (sarahwilliams -> oliviamurphy) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Reminder: Client Call at 3 PM"
email_body = (
    "Thanks for the reminder, Olivia! I have got my notes ready, and I will join the call a bit early as well.\n"
    "Hopefully, we can clear up their concerns quickly.\n\n"
    "See you on the call,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=43, seconds=12))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = oliviamurphy_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Retrieve some data from budget_info with johndoe
print("\n---------- Retrieve some data from budget_info with johndoe ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = johndoe_computer2
database_username = "johndoe"
database_password = "john"
table_name = "budget_info"
database_name = "evil_corp"
user = "johndoe"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Reply to reply email (sarahwilliams -> elliotalderson)
print("\n---------- Reply to reply email (sarahwilliams -> elliotalderson) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Follow-Up on Files"
email_body = (
    "Tuesday works for me. Lets plan for 10 AM.\n"
    "I can prepare a brief presentation on the potential outcomes.\n\n"
    "Looking forward to wrapping this up!\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=27, seconds=27))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = elliotalderson_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject, first=False)

# Sleep
time.sleep(5)

###########################################################
# Retrieve some data from contact_information with johndoe
print("\n---------- Retrieve some data from contact_information with johndoe ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = johndoe_computer2
database_username = "johndoe"
database_password = "john"
table_name = "contact_information"
database_name = "evil_corp"
user = "johndoe"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Send email (johndoe -> sarahwilliams)
print("\n---------- Send email (johndoe -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Project Update Meeting"
email_body = (
    "Hi Sarah,\n"
    "I wanted to confirm the agenda for our project update meeting next week.\n"
    "I think we need to discuss the recent feedback from the client and how we will approach the next phases.\n\n"
    "Can we chat about this Monday morning?\n\n"
    "Best,\nJohn\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=56, seconds=3))

# Set the parameter for the functions
container = johndoe_computer2
receiver = sarahwilliams_email
sender = "johndoe"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)
