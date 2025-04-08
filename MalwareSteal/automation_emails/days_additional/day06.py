import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 6 ##########################

print("\n-------------- DAY 6 (Data Breach) --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=5, minutes=5, seconds=45))

print("Starting date DAY 6: ", fake_date, "\n")

###########################################################
# Send email (sampointer -> sarahwilliams)
print("\n---------- Send email (sampointer -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Software Patch Rollout"
email_body = (
    "Hi Sarah,\n"
    "We are planning to roll out a new software patch next Thursday.\n"
    "There might be minor adjustments required on your end for compatibility.\n"
    "I will tell you more details as soon as we meet.\n\n"
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
# Retrieve some data from budget_info with jakethompson
print("\n---------- Retrieve some data from budget_info with jakethompson ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = jakethompson_pc2
database_username = "jakethompson"
database_password = "jake"
table_name = "budget_info"
database_name = "evil_corp"
user = "jakethompson"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Send email (emilycarter -> sarahwilliams)
print("\n---------- Send email (emilycarter -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Follow-Up on Action Items"
email_body = (
    "Hi Sarah,\n"
    "Just a quick follow-up on our action items from the last meeting.\n"
    "Have you had a chance to finalize the budget report? We need it for our presentation next week.\n\n"
    "Thanks!\n\n"
    "Best,\nEmily\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=33, seconds=23))

# Set the parameter for the functions
container = emilycarter_computer3
receiver = sarahwilliams_email
sender = "emilycarter"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
# Retrieve some data from project_info with jamesfoster
print("\n---------- Retrieve some data from project_info with jamesfoster ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = jamesfoster_computer4
database_username = "jamesfoster"
database_password = "james"
table_name = "project_info"
database_name = "evil_corp"
user = "jamesfoster"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Insert some data in the database with sarahwilliams
print("\n---------- Insert some data in the database with sarahwilliams ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=4, seconds=33))

container = sarahwilliams_computer1
database_username = "sarahwilliams"
database_password = "sarah"
table_name = "key_measurements"
database_name = "evil_corp"
user = "sarahwilliams"
section = "Performance"
detail = "Website Load Time"
sub_detail = "Average load time: 1.2 seconds over the past week."

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
insert_data(container, fake_date, database_username, database_password, table_name, database_name, user, section, detail, sub_detail)

time.sleep(5)

###########################################################
# Reply to reply email (sarahwilliams -> johndoe)
print("\n---------- Reply to reply email (sarahwilliams -> johndoe) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Project Status"
email_body = (
    "Perfect, I will be ready to chat at 5 PM. Thanks for the quick response!\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=22, seconds=23))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = johndoe_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject, first=False)

# Sleep
time.sleep(5)
