import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 4 ##########################

print("\n-------------- DAY 4 --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=3, minutes=1, seconds=1))

print("Starting date DAY 4: ", fake_date, "\n")

###########################################################
# Reply email (sarahwilliams -> sampointer)
print("\n---------- Reply email (sarahwilliams -> sampointer) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Server Maintenance Schedule"
email_body = (
    "Hi Sam,\n\n"
    "Thanks for the notice! There is an ongoing project I am involved with that could be affected.\n"
    "Can we coordinate to ensure minimal impact? I can provide a list of priority systems to keep running during the maintenance.\n\n"
    "Best,\nSarah\n"
)

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = sampointer_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Reply email (sarahwilliams -> johndoe)
print("\n---------- Reply email (sarahwilliams -> johndoe) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Data Discrepancies"
email_body = (
    "Hi John,\n\n"
    "Thanks for pointing this out. I will review the data today and see if there is anything we need to flag with the finance team.\n"
    "I will get back to you by the end of the day.\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=22, seconds=33))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = johndoe_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Send email (sarahwilliams -> emilycarter)
print("\n---------- Send email (sarahwilliams -> emilycarter) ----------")

# Set the email arguments
email_subject = "Proposal Review Meeting"
email_body = (
    "I hope this email finds you well. I have completed the initial draft of the proposal for the upcoming client presentation.\n\n"
    "Thank you!\n\n"
    "Best regards,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=11, seconds=20))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = emilycarter_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
# Insert some data in the database with emilycarter
print("\n---------- Insert some data in the database with emilycarter ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=4, seconds=33))

container = emilycarter_computer3
database_username = "emilycarter"
database_password = "emily"
table_name = "contact_information"
database_name = "evil_corp"
user = "emilycarter"
section = "Client"
detail = "Acme Corp"
sub_detail = "Primary contact: Johnny Redd, Email: johhnyredd@acme.com, Phone: +123456789"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
insert_data(container, fake_date, database_username, database_password, table_name, database_name, user, section, detail, sub_detail)

time.sleep(5)

###########################################################
# Reply email (emilycarter -> sarahwilliams)
print("\n---------- Reply email (emilycarter -> sarahwilliams) ----------")

# Retrieve the email with emilycarter
save_email(emilycarter_computer3)

# Set the email arguments
email_subject = "Re: Proposal Review Meeting"
email_body = (
    "Hi Sarah,\n\n"
    "Thanks for pointing this out. I will review the data today and see if there is anything we need to flag with the finance team.\n"
    "I will get back to you by the end of the day.\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=22, seconds=33))

# Set the parameter for the functions
container = emilycarter_computer3
receiver = sarahwilliams_email
sender = "emilycarter"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Send email (sarahwilliams -> jakethompson)
print("\n---------- Send email (sarahwilliams -> jakethompson) ----------")

# Set the email arguments
email_subject = "New Office Equipment Request"
email_body = (
    "Hi Jake,\n"
    "I have been receiving requests from a few team members about upgrading their office equipment, particularly monitors and keyboards.\n"
    "I wanted to check in with you first, do you know if we have the budget for this in Q4?\n"
    "If not, is there room to shuffle some resources around to cover the costs?\n\n"
    "Let me know your thoughts when you get a chance.\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=2, minutes=15, seconds=25))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = jakethompson_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
# Reply email (jakethompson -> sarahwilliams)
print("\n---------- Reply email (jakethompson -> sarahwilliams) ----------")

# Retrieve the email with jakethompson
save_email(jakethompson_pc2)

# Set the email arguments
email_subject = "Re: New Office Equipment Request"
email_body = (
    "Hi Sarah,\n\n"
    "We should be able to cover most of the requests.\n"
    "I will need to take a closer look at the current budget allocation, but I think we can move some funds from the operations budget to handle the equipment upgrades.\n"
    "I will confirm tomorrow after reviewing the latest financials.\n\n"
    "Best,\nJake\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=2, minutes=45, seconds=23))

# Set the parameter for the functions
container = jakethompson_pc2
receiver = sarahwilliams_email
sender = "jakethompson"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

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
