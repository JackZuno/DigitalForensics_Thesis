import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 9 ##########################

print("\n-------------- DAY 9 (Data Breach) --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=8, minutes=1, seconds=23))

print("Starting date DAY 9: ", fake_date, "\n")

###########################################################
# Extract info from locations table
print("\n---------- Extract info from locations table ----------")

query = f"SELECT * FROM {locations_table};"
database_name = "evil_corp"
user = "sarahwilliams"

# Set fake time on the database server and computer and run the query
set_fake_time(database_server_container, fake_date)
set_fake_time(sarahwilliams_computer1, fake_date)
query_fakedate(sarahwilliams_computer1, fake_date, username_db, password_db, locations_table, database_name, query, user)

# Sleep
time.sleep(5)

###########################################################
# Retrieve some data from team_involved with oliviamurphy
print("\n---------- Retrieve some data from team_involved with oliviamurphy ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=5, seconds=31))

container = oliviamurphy_pc4
database_username = "oliviamurphy"
database_password = "olivia"
table_name = "team_involved"
database_name = "evil_corp"
user = "oliviamurphy"

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
retrieve_data(container, fake_date, database_username, database_password, table_name, database_name, user)

time.sleep(5)

###########################################################
# Extract info from team_involved table
print("\n---------- Extract info from team_involved table ----------")

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=16, seconds=32))

query = f"SELECT * FROM {team_involved_table};"
database_name = "evil_corp"
user = "sarahwilliams"

# Set fake time on the database server and computer and run the query
set_fake_time(database_server_container, fake_date)
set_fake_time(sarahwilliams_computer1, fake_date)
query_fakedate(sarahwilliams_computer1, fake_date, username_db, password_db, team_involved_table, database_name, query, user)

# Sleep
time.sleep(5)

###########################################################
# Merge the files
print("\n---------- Merge the files ----------")

input_folder = "/home/sarahwilliams/personalStuff"
destination_folder = "/home/sarahwilliams/personalStuff/doctorApp"
output_filename = "doctor_appointment.csv"
user = "sarahwilliams"

# Set fake time on the database server and computer and run the merge file function
set_fake_time(sarahwilliams_computer1, fake_date)
merge_files(sarahwilliams_computer1, user, input_folder, destination_folder, output_filename)

###########################################################
# Send email (sarahwilliams -> elliotalderson)
print("\n---------- Send email (sarahwilliams -> elliotalderson) ----------")

# Set the email arguments
email_subject = "Important Files"
email_body = (
    "Hey Elliot,\n"
    "I have compiled the files we discussed.\n"
    "They contain the sensitive data we need. Please find them attached.\n\n"
    "Let me know if everything looks good on your end.\n\n"
    "Best,\nSarah\n"
)

# Set fake time on the server and send the email
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=46, seconds=23))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = elliotalderson_email
sender = "sarahwilliams"

# Attachment
attachment_path = "/home/sarahwilliams/personalStuff/doctorApp/doctor_appointment.csv"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_with_attach(container, fake_date, receiver, email_subject, email_body, sender, attachment_path)

# Sleep
time.sleep(5)

# Delete the file
delete_file_and_folder(container, user, "doctorApp")

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
table_name = "project_info"
database_name = "evil_corp"
user = "emilycarter"
section = "Product Development"
detail = "Smartwatch"
sub_detail = "Launching a new smartwatch with health-tracking features."

# Set fake time on the server and run the query
set_fake_time(database_server_container, fake_date)
insert_data(container, fake_date, database_username, database_password, table_name, database_name, user, section, detail, sub_detail)

time.sleep(5)

###########################################################
# Reply email (elliotalderson -> sarahwilliams)
print("\n---------- Reply email (elliotalderson -> sarahwilliams) ----------")

# Retrieve the email with elliotalderson
save_email(elliotalderson_attacker)

# Set the email arguments
email_subject = "Re: Important Files"
email_body = (
    "Thanks, Sarah!\n\n"
    "I will review these right away. This could be the breakthrough we need.\n"
    "I appreciate your hard work on this.\n\n"
    "Talk soon,\nElliot\n"
)

# Select the fake date
date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=2, minutes=22, seconds=22))

# Set the parameter for the functions
container = elliotalderson_attacker
receiver = sarahwilliams_email
sender = "elliotalderson"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)
