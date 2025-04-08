import time
from write_emails import *
from database_actions.faketime_operations import *
from datetime import datetime, timedelta

########################## DAY 1 ##########################

print("\n-------------- DAY 1 --------------")

# Select the fake date
fake_date = initial_fake_date

print("Starting date DAY 1: ", fake_date, "\n")

###########################################################
# Send email (sarahwilliams -> jakethompson)
print("\n---------- Send email (sarahwilliams -> jakethompson) ----------")

# Set the email arguments
email_subject = "Feedback on Software Update"
email_body = (
    "Hi Jake,\n\n"
    "I hope you are doing well. I wanted to get your thoughts on the latest software update "
    "for our internal tools. Have you had a chance to explore the new features?\n"
    "If you have any insights or feedback, I would appreciate hearing your perspective "
    "before our team meeting next week.\n\n"
    "Thanks in advance!\n\n"
    "Best Regards,\nSarah\n"
)

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
# Send email (emilycarter -> sarahwilliams)
print("\n---------- Send email (emilycarter -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Project Timeline Review"
email_body = (
    "Hi Sarah,\n\n"
    "I wanted to touch base regarding the project timelines."
    "We need to ensure that everything is on track for the upcoming deadlines.\n"
    "Can we schedule a meeting to review the current status?\n\n"
    "Let me know what works for you!\n\n"
    "Best,\nEmily\n"
)

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=4, seconds=33))

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
# Insert some data in the database with jamesfoster
print("\n---------- Insert some data in the database with jamesfoster ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=4, seconds=33))

container = jamesfoster_computer4
database_username = "jamesfoster"
database_password = "james"
table_name = "project_info"
database_name = "evil_corp"
user = "jamesfoster"
section = "AI Research"
detail = "Natural Language Processing"
sub_detail = "Developing a chatbot to handle customer service queries."

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
insert_data(container, fake_date, database_username, database_password, table_name, database_name, user, section, detail, sub_detail)

time.sleep(5)

###########################################################
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

###########################################################
# Reply email (jakethompson -> sarahwilliams)
print("\n---------- Reply email (jakethompson -> sarahwilliams) ----------")

# Retrieve the email with jakethompson
save_email(jakethompson_pc2)

# Set the email arguments
email_subject = "Re: Feedback on Software Update"
email_body = (
    "Hi Sarah,\n\n"
    "I have tested the new features briefly. There are a couple of areas where the user interface could be more intuitive, "
    "but overall, I think the improvements are great.\n"
    "I will give you a more detailed review later today when we meet up.\n\n"
    "Cheers,\nJake\n"
)

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=12, seconds=43))

# Set the parameter for the functions
container = jakethompson_pc2
receiver = sampointer_email
sender = "jakethompson"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Retrieve some data from project_info with annamoore
print("\n---------- Retrieve some data from project_info with annamoore ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = annamoore_pc3
database_username = "annamoore"
database_password = "anna"
table_name = "project_info"
database_name = "evil_corp"
user = "annamoore"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Send email (sarahwilliams -> sampointer)
print("\n---------- Send email (sarahwilliams -> sampointer) ----------")

# Set the email arguments
email_subject = "Budget Allocation for Next Quarter"
email_body = (
    "Hi Sam,\n\n"
    "I have been going through the budget projections for the next quarter, and I noticed a few areas that need further clarification.\n"
    "Would you be able to join a brief call tomorrow at 2 PM to discuss the allocation for the marketing initiatives?\n"
    "I want to ensure we are aligned before we finalize the numbers.\n\n"
    "Let me know if that works for you.\n\n"
    "Best,\nSarah\n"
)

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, seconds=43))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = sampointer_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
# Retrieve some data from key_measurements with jakethompson
print("\n---------- Retrieve some data from key_measurements with jakethompson ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = jakethompson_pc2
database_username = "jakethompson"
database_password = "jake"
table_name = "key_measurements"
database_name = "evil_corp"
user = "jakethompson"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)
