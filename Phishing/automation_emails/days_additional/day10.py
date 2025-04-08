import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 10 ##########################

print("\n-------------- DAY 10 (Phishing) --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=9, minutes=2, seconds=45))

print("Starting date DAY 10: ", fake_date, "\n")

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

###########################################################
# Retrieve some data from contact_information with elliotalderson
print("\n---------- Retrieve some data from contact_information with elliotalderson (Phishing) ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = elliotalderson_attacker
database_username = "sarahwilliams"
database_password = "sarah"
table_name = "contact_information"
database_name = "evil_corp"
user = "elliotalderson"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)
