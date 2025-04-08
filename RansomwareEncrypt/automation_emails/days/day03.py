import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 3 ##########################

print("\n-------------- DAY 3 --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=2, minutes=4, seconds=16))

print("Starting date DAY 3: ", fake_date, "\n")

###########################################################
# Send email (johndoe -> sarahwilliams)
print("\n---------- Send email (johndoe -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Data Discrepancies"
email_body = (
    "Hi Sarah,\n\n"
    "I noticed some discrepancies in the latest data from the finance team.\n"
    "I am not sure if it is just a minor issue or something bigger. Can you have a look when you get a chance?\n\n"
    "Best,\nJohn\n"
)

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
# Retrieve some data from team_involved with sampointer
print("\n---------- Retrieve some data from team_involved with sampointer ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = sampointer_pc1
database_username = "sampointer"
database_password = "sam"
table_name = "team_involved"
database_name = "evil_corp"
user = "sampointer"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Send email (sarahwilliams -> oliviamurphy)
print("\n---------- Send email (sarahwilliams -> oliviamurphy) ----------")

# Set the email arguments
email_subject = "Monthly Report Submission"
email_body = (
    "Hi Olivia,\n\n"
    "I hope everything is going smoothly with the report. I wanted to check in on the status of the monthly report submission.\n"
    "We will need it by Friday for the executive review, so if you need any assistance or an extra set of eyes, feel free to reach out!\n"
    "Looking forward to hearing from you.\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=11, seconds=20))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = oliviamurphy_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
# Reply email (oliviamurphy -> sarahwilliams)
print("\n---------- Reply email (oliviamurphy -> sarahwilliams) ----------")

# Retrieve the email with oliviamurphy
save_email(oliviamurphy_pc4)

# Set the email arguments
email_subject = "Re: Monthly Report Submission"
email_body = (
    "Hi Sarah,\n\n"
    "Thanks for checking in! The report is almost done, I am just finalizing a few sections.\n"
    "I will send it over for review by Thursday afternoon so we have some buffer time in case we need revisions.\n\n"
    "Best,\nOlivia\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=45, seconds=55))

# Set the parameter for the functions
container = oliviamurphy_pc4
receiver = sarahwilliams_email
sender = "oliviamurphy"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Reply email (sarahwilliams -> emilycarter)
print("\n---------- Reply email (sarahwilliams -> emilycarter) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Project Timeline Review"
email_body = (
    "Hi Emily,\n\n"
    "I am so sorry but I missed the email, I hope everything is going well.\n"
    "I am available tomorrow afternoon if that works for you. I will gather all the necessary updates beforehand.\n\n"
    "Thanks for following up!\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=55, seconds=55))

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
# Retrieve some data from budget_info with sampointer
print("\n---------- Retrieve some data from budget_info with sampointer ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = sampointer_pc1
database_username = "sampointer"
database_password = "sam"
table_name = "budget_info"
database_name = "evil_corp"
user = "sampointer"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Send email (sampointer -> sarahwilliams)
print("\n---------- Send email (sampointer -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Server Maintenance Schedule"
email_body = (
    "Hi Sarah,\n\n"
    "Just wanted to give you a heads-up that we are planning some server maintenance next week. This might cause brief downtimes.\n"
    "Let me know if there is any critical system that should not be affected during that time.\n\n"
    "Best,\nSam\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=11, seconds=20))

# Set the parameter for the functions
container = sampointer_pc1
receiver = sarahwilliams_email
sender = "sampointer"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)