import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 7 ##########################

print("\n-------------- DAY 7 (Data Breach) --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=6, minutes=2, seconds=45))

print("Starting date DAY 7: ", fake_date, "\n")

###########################################################
# Retrieve some data from locations with sampointer
print("\n---------- Retrieve some data from locations with sampointer ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = sampointer_pc1
database_username = "sampointer"
database_password = "sam"
table_name = "locations"
database_name = "evil_corp"
user = "sampointer"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Reply email (sarahwilliams -> sampointer)
print("\n---------- Reply email (sarahwilliams -> sampointer) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Software Patch Rollout"
email_body = (
    "Hi Sam,\n\n"
    "Thursday sounds good.\n"
    "I will review the details once you send them over and make sure everything is ready on our end.\n\n"
    "Thanks for the heads-up!\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=15, seconds=43))

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
# Reply email (sarahwilliams -> emilycarter)
print("\n---------- Reply email (sarahwilliams -> emilycarter) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Follow-Up on Action Items"
email_body = (
    "Hi Emily,\n\n"
    "Yes, I am wrapping up the budget report today.\n"
    "I will send it over by the end of the day so we can review it together before the presentation.\n\n"
    "Thanks for the reminder!\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=15, seconds=43))

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
# Send email (sarahwilliams -> sampointer)
print("\n---------- Send email (sarahwilliams -> sampointer) ----------")

# Set the email arguments
email_subject = "Need a Favor"
email_body = (
    "Hi Sam,\n"
    "Hope you are doing well! I am running some maintenance checks on some projects, but I have hit a small snag.\n"
    "My access credentials are not working and I need to check this fiel ASAP.\n"
    "Would it be possible for me to borrow your login just for a quick check?\n"
    "I promise it will not take long, and I will be sure to log out as soon as I am done.\n\n"
    "Let me know if you are okay with this.\n\n"
    "Thanks a bunch,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=2, minutes=46, seconds=23))

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
# Insert some data in the database with annamoore
print("\n---------- Insert some data in the database with annamoore ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=4, seconds=33))

container = annamoore_pc3
database_username = "annamoore"
database_password = "anna"
table_name = "locations"
database_name = "evil_corp"
user = "annamoore"
section = "Offices"
detail = "New York"
sub_detail = "Opened a new office in downtown Manhattan."

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
insert_data(container, fake_date, database_username, database_password, table_name, database_name, user, section, detail, sub_detail)

time.sleep(5)

###########################################################
# Reply email (sampointer -> sarahwilliams)
print("\n---------- Reply email (sampointer -> sarahwilliams) ----------")

# Retrieve the email with sampointer
save_email(sampointer_pc1)

# Set the email arguments
email_subject = "Re: Need a Favor"
email_body = (
    "Hi Sarah,\n\n"
    "I would prefer not to share my credentials over email for security reasons, but I can help you out.\n"
    "Lets meet tomorrow in the break room around 11 AM, and I will give you what you need in person.\n\n"
    "See you then,\nSam\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=15, seconds=43))

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
# Send email (sarahwilliams -> oliviamurphy)
print("\n---------- Send email (sarahwilliams -> oliviamurphy) ----------")

# Set the email arguments
email_subject = "Team Meeting Prep"
email_body = (
    "Hi Olivia,\n"
    "I am putting together the agenda for our team meeting on Friday.\n"
    "Could you please send me a brief update on the status of the new client onboarding?\n"
    "I want to make sure we address any concerns during the discussion.\n\n"
    "Thanks a lot,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=52, seconds=54))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = oliviamurphy_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)
