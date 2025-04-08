import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 8 ##########################

print("\n-------------- DAY 8 (Data Breach) --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=7, minutes=5, seconds=22))

print("Starting date DAY 8: ", fake_date, "\n")

###########################################################
# Reply email (oliviamurphy -> sarahwilliams)
print("\n---------- Reply email (oliviamurphy -> sarahwilliams) ----------")

# Retrieve the email with oliviamurphy
save_email(oliviamurphy_pc4)

# Set the email arguments
email_subject = "Re: Team Meeting Prep"
email_body = (
    "Hi Sarah,\n\n"
    "Sure thing! I will get that over to you by tomorrow morning.\n"
    "So far, things are moving smoothly, but there are a few small issues I want to flag for us to discuss.\n"
    "I will include those in the update.\n\n"
    "Looking forward to the meeting,\nOlivia\n"
)

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
# Reply email (sarahwilliams -> sampointer)
print("\n---------- Reply email (sarahwilliams -> sampointer) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Need a Favor"
email_body = (
    "Hey Sam,\n\n"
    "That sounds perfect. I totally understand about the security concerns.\n"
    "I will see you at 11. Thanks so much for helping me out with this!\n\n"
    "Best,\nSarah\n"
)

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=22, seconds=22))

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
# Send email (annamoore -> sarahwilliams)
print("\n---------- Send email (annamoore -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Lunch?"
email_body = (
    "Hey Sarah,\n"
    "It is been a hectic week, and I could use a break.\n"
    "Are you free for lunch tomorrow? I am thinking of trying that new café around the corner.\n"
    "Let me know if you are up for it!\n\n"
    "Cheers,\nAnna\n"
)

# Set fake time on the server and send the email
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=46, seconds=23))

# Set the parameter for the functions
container = annamoore_pc3
receiver = sarahwilliams_email
sender = "annamoore"

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
# Reply email (sarahwilliams -> annamoore)
print("\n---------- Reply email (sarahwilliams -> annamoore) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Lunch?"
email_body = (
    "Hey Anna,\n\n"
    "I would love to! Tomorrow works for me, and I have been meaning to check that place out.\n"
    "Lets plan for 12:30 PM?\n\n"
    "See you then!,\nSarah\n"
)

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=2, minutes=22, seconds=22))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = annamoore_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Extract info from project_info table
print("\n---------- Extract info from project_info table ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=42, seconds=24))

query = f"SELECT * FROM {project_info_table};"
database_name = "evil_corp"
user = "sarahwilliams"

# Set fake time on the database server and computer and run the query
set_fake_time(database_server_container, fake_date)
set_fake_time(sarahwilliams_computer1, fake_date)
query_fakedate(sarahwilliams_computer1, fake_date, username_db, password_db, project_info_table, database_name, query, user)

# Sleep
time.sleep(5)

###########################################################
# Extract info from budget_info table
print("\n---------- Extract info from budget_info table ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=2, minutes=42, seconds=24))

query = f"SELECT * FROM {budget_info_table};"
database_name = "evil_corp"
user = "sarahwilliams"

# Set fake time on the database server and computer and run the query
set_fake_time(database_server_container, fake_date)
set_fake_time(sarahwilliams_computer1, fake_date)
query_fakedate(sarahwilliams_computer1, fake_date, username_db, password_db, budget_info_table, database_name, query, user)

# Sleep
time.sleep(5)

###########################################################
# Insert some data in the database with sampointer
print("\n---------- Insert some data in the database with sampointer ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=4, seconds=33))

container = sampointer_pc1
database_username = "sampointer"
database_password = "sam"
table_name = "team_involved"
database_name = "evil_corp"
user = "sampointer"
section = "Development"
detail = "Backend Team"
sub_detail = "Responsible for creating the API services for the new mobile app."

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
insert_data(container, fake_date, database_username, database_password, table_name, database_name, user, section, detail, sub_detail)

time.sleep(5)

###########################################################
# Extract info from contact_information table
print("\n---------- Extract info from contact_information table ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours= 1, minutes=33, seconds=14))

query = f"SELECT * FROM {contact_information_table};"
database_name = "evil_corp"
user = "sarahwilliams"

# Set fake time on the database server and computer and run the query
set_fake_time(database_server_container, fake_date)
set_fake_time(sarahwilliams_computer1, fake_date)
query_fakedate(sarahwilliams_computer1, fake_date, username_db, password_db, contact_information_table, database_name, query, user)

# Sleep
time.sleep(5)

###########################################################
# Insert some data in the database with sampointer
print("\n---------- Insert some data in the database with sampointer ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=4, seconds=33))

container = sampointer_pc1
database_username = "sampointer"
database_password = "sam"
table_name = "locations"
database_name = "evil_corp"
user = "sampointer"
section = "Offices"
detail = "San Francisco"
sub_detail = "Opened a new satellite office in the San Francisco Bay Area."

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
insert_data(container, fake_date, database_username, database_password, table_name, database_name, user, section, detail, sub_detail)

time.sleep(5)

###########################################################
# Extract info from key_measurements table
print("\n---------- Extract info from key_measurements table ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=44, seconds=4))

query = f"SELECT * FROM {key_measurements_table};"
database_name = "evil_corp"
user = "sarahwilliams"

# Set fake time on the database server and computer and run the query
set_fake_time(database_server_container, fake_date)
set_fake_time(sarahwilliams_computer1, fake_date)
query_fakedate(sarahwilliams_computer1, fake_date, username_db, password_db, key_measurements_table, database_name, query, user)

# Sleep
time.sleep(5)
