import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 11 ##########################

print("\n-------------- DAY 11 (Phishing) --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=10, minutes=5, seconds=28))

print("Starting date DAY 11: ", fake_date, "\n")

###########################################################
# Retrieve some data from contact_information with elliotalderson
print("\n---------- Retrieve some data from contact_information with elliotalderson (Phishing) ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = elliotalderson_attacker
database_username = "johndoe"
database_password = "john"
table_name = "project_info"
database_name = "evil_corp"
user = "elliotalderson"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Reply email (sarahwilliams -> johndoe)
print("\n---------- Reply email (sarahwilliams -> johndoe) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Project Update Meeting"
email_body = (
    "Hi John,\n\n"
    "Yes, absolutely. Monday morning sounds good.\n"
    "I will prepare the latest metrics to share.\n\n"
    "Lets touch base around 9 AM?\n\n"
    "Best,\nSarah\n"
)

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
# Retrieve some data from locations with elliotalderson
print("\n---------- Retrieve some data from locations with elliotalderson (Phishing) ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = elliotalderson_attacker
database_username = "emilycarter"
database_password = "emily"
table_name = "locations"
database_name = "evil_corp"
user = "elliotalderson"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Send email (emilycarter -> sarahwilliams, sampointer)
print("\n---------- Send email (emilycarter -> sarahwilliams, sampointer) ----------")

# Set the email arguments
email_subject = "Team Lunch on Friday"
email_body = (
    "Hi Sarah, Hi Sam,\n"
    "I wanted to let you both know that we are organizing a team lunch this Friday.\n"
    "It will be a nice break to connect and catch up.\n\n"
    "Let me know if you are free to join!\n\n"
    "Best,\nEmily\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=56, seconds=3))

# Set the parameter for the functions
container = emilycarter_computer3
receiver = f"{sarahwilliams_email} {sampointer_email}"
sender = "emilycarter"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
# Retrieve some data from key_measurements with elliotalderson
print("\n---------- Retrieve some data from key_measurements with elliotalderson (Phishing) ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = elliotalderson_attacker
database_username = "johndoe"
database_password = "john"
table_name = "key_measurements"
database_name = "evil_corp"
user = "elliotalderson"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

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
section = "Operations"
detail = "Facility Upgrade"
sub_detail = "Budget of $50,000 allocated for upgrading factory machinery."

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
insert_data(container, fake_date, database_username, database_password, table_name, database_name, user, section, detail, sub_detail)

time.sleep(5)

###########################################################
# Retrieve some data from budget_info with elliotalderson
print("\n---------- Retrieve some data from budget_info with elliotalderson (Phishing) ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = elliotalderson_attacker
database_username = "emilycarter"
database_password = "emily"
table_name = "budget_info"
database_name = "evil_corp"
user = "elliotalderson"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Send email (emilycarter -> sarahwilliams)
print("\n---------- Send email (emilycarter -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Resource Allocation for Next Quarter"
email_body = (
    "Hi Sarah,\n"
    "As we are planning for the next quarter, I wanted to touch base on resource allocation.\n"
    "Can we schedule some time to review the current plan and make adjustments if needed?\n\n"
    "Looking forward to your input.\n\n"
    "Best,\nEmily\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=51, seconds=39))

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
# Retrieve some data from project_info with elliotalderson
print("\n---------- Retrieve some data from project_info with elliotalderson (Phishing) ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = elliotalderson_attacker
database_username = "sarahwilliams"
database_password = "sarah"
table_name = "project_info"
database_name = "evil_corp"
user = "elliotalderson"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Insert some data in the database with sampointer
print("\n---------- Insert some data in the database with emilycarter ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=4, seconds=33))

container = sampointer_pc1
database_username = "sampointer"
database_password = "sam"
table_name = "contact_information"
database_name = "evil_corp"
user = "sampointer"
section = "Clients"
detail = "GlobalTech Inc."
sub_detail = "Primary contact: Sarah Lee, Email: sarah.lee@globaltech.com, Phone: +1987654321"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
insert_data(container, fake_date, database_username, database_password, table_name, database_name, user, section, detail, sub_detail)

time.sleep(5)

###########################################################
# Reply email (sampointer -> emilycarter, sarahwilliams)
print("\n---------- Reply email (sampointer -> emilycarter, sarahwilliams) ----------")

# Retrieve the email with sampointer
save_email(sampointer_pc1)

# Set the email arguments
email_subject = "Re: Team Lunch on Friday"
email_body = (
    "Hi Emily\n\n"
    "Count me in! It will be great to catch up with everyone outside of work for a bit.\n\n"
    "Best,\nSam\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=27, seconds=27))

# Set the parameter for the functions
container = sampointer_pc1
receiver = f"{emilycarter_email}, {sarahwilliams_email}"
sender = "sampointer"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Reply to reply email (sarahwilliams -> emilycarter, sampointer)
print("\n---------- Reply to reply email (sarahwilliams -> emilycarter, sampointer) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Team Lunch on Friday"
email_body = (
    "Hi Emily\n\n"
    "That sounds fun! I am definitely in as well. Looking forward to it.\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=11, seconds=11))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = f"{emilycarter_email}, {sampointer_email}"
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

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
table_name = "key_measurements"
database_name = "evil_corp"
user = "jamesfoster"
section = "Production"
detail = "Machine Efficiency"
sub_detail = "Average efficiency: 85 percent across all machines for Q1."

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
insert_data(container, fake_date, database_username, database_password, table_name, database_name, user, section, detail, sub_detail)

time.sleep(5)

###########################################################
# Reply to reply email (johndoe -> sarahwilliams)
print("\n---------- Reply to reply email (johndoe -> sarahwilliams) ----------")

# Retrieve the email with johndoe
save_email(johndoe_computer2)

# Set the email arguments
email_subject = "Re: Project Update Meeting"
email_body = (
    "Yes, it is perfect.\n\n"
    "Best,\nJohn\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=13, seconds=19))

# Set the parameter for the functions
container = johndoe_computer2
receiver = sarahwilliams_email
sender = "johndoe"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject, first=False)

# Sleep
time.sleep(5)
