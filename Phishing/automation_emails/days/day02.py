import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 2 ##########################

print("\n-------------- DAY 2 --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=1, minutes=11, seconds=4))

print("Starting date DAY 2: ", fake_date, "\n")

###########################################################
# Send email (sarahwilliams -> annamoore)
print("\n---------- Send email (sarahwilliams -> annamoore) ----------")

# Set the email arguments
email_subject = "Client Meeting Preparation"
email_body = (
    "Hi Anna,\n\n"
    "I hope you are having a great day! Just a quick note to confirm that we are on track for the client meeting on Friday.\n"
    "I have shared the latest version of the presentation with you.\n"
    "Can you take a look and let me know if there are any points that need adjustment?\n"
    "Also, please make sure the numbers in the final slides are correct.\n\n"
    "Thanks,\nSarah\n"
)

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = annamoore_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
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

###########################################################
# Retrieve some data from locations with oliviamurphy
print("\n---------- Retrieve some data from locations with oliviamurphy ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = oliviamurphy_pc4
database_username = "oliviamurphy"
database_password = "olivia"
table_name = "locations"
database_name = "evil_corp"
user = "oliviamurphy"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Reply email (sampointer -> sarahwilliams)
print("\n---------- Reply email (sampointer -> sarahwilliams) ----------")

# Retrieve the email with sampointer
save_email(sampointer_pc1)

# Set the email arguments
email_subject = "Re: Budget Allocation for Next Quarter"
email_body = (
    "Hi Sarah,\n\n"
    "2 PM tomorrow works for me. I will have the updated figures ready for review.\n"
    "Let me know if there's anything specific you'd like me to focus on ahead of the call.\n\n"
    "Best,\nSam\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=12, seconds=44))

# Set the parameter for the functions
container = sampointer_pc1
receiver = sarahwilliams_email
sender = "sampointer"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Reply email (annamoore -> sarahwilliams)
print("\n---------- Reply email (annamoore -> sarahwilliams) ----------")

# Retrieve the email with annamoore
save_email(annamoore_pc3)

# Set the email arguments
email_subject = "Re: Client Meeting Preparation"
email_body = (
    "Hi Sarah,\n\n"
    "Yes, we are on track. I have reviewed the presentation, and everything looks good so far.\n"
    "I will double-check the numbers and let you know if there is anything off, but they seem accurate at a glance.\n\n"
    "Thanks for sharing this in advance!\n\n"
    "Best,\nAnna\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=2, minutes=44, seconds=33))

# Set the parameter for the functions
container = annamoore_pc3
receiver = sarahwilliams_email
sender = "annamoore"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Send email (sarahwilliams -> jamesfoster)
print("\n---------- Send email (sarahwilliams -> jamesfoster) ----------")

# Set the email arguments
email_subject = "Team Collaboration Meeting"
email_body = (
    "Hi James,\n\n"
    "I hope you are having a productive week. I wanted to check in regarding our team collaboration strategy for the new project.\n"
    "Are you available for a brief meeting tomorrow afternoon to brainstorm ideas and delegate tasks?\n"
    "Looking forward to your input.\n\n"
    "Best regards,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=2, minutes=11, seconds=40))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = jamesfoster_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
# Reply email (jamesfoster -> sarahwilliams)
print("\n---------- Reply email (jamesfoster -> sarahwilliams) ----------")

# Retrieve the email with jamesfoster
save_email(jamesfoster_computer4)

# Set the email arguments
email_subject = "Re: Team Collaboration Meeting"
email_body = (
    "Hi Sarah,\n\n"
    "Yes, we can do it. There are some important news I would like to tell you in person\n\n"
    "Talk soon,\nJames\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=30, seconds=33))

# Set the parameter for the functions
container = jamesfoster_computer4
receiver = sarahwilliams_email
sender = "jamesfoster"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

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
table_name = "budget_info"
database_name = "evil_corp"
user = "emilycarter"
section = "Marketing"
detail = "Ad Campaign"
sub_detail = "Allocated budget of $10,000 for Q1 advertising campaigns."

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
insert_data(container, fake_date, database_username, database_password, table_name, database_name, user, section, detail, sub_detail)

time.sleep(5)
