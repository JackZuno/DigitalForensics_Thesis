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
# Zip the ransomware and then send it via email

print("\n---------- ZIP the ransomware folder ----------")

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=44, seconds=23))

container = elliotalderson_attacker

# Set the fake date and time and then zip the file
set_fake_time(container, fake_date)
zip_ransomware_folder(container)

time.sleep(10)

###########################################################
# Send it via email

print("\n---------- Send ransomware via email (elliotalderson -> sarahwilliams, sampointer, emilycarter) ----------")

# Set the email arguments
email_subject = "Important Security Update: Action Required"
email_body = (
    "Dear Team,\n"
    "We are reaching out to inform you of an important security update that is now available.\n"
    "This update includes security improvements and enhances the overall performance of the application.\n"
    "Please install this update as soon as possible to keep your software secure and up to date.\n\n"
    "To install the update, please follow these steps:\n"
    "1. Download the attached ZIP file to your device.\n"
    "2. Extract the contents of the ZIP file.\n"
    "3. Open the folder and follow the instructions provided in the \"ReadMe\" file to complete the installation.\n\n"
    "If you have any questions or need assistance, please contact our support team at support@e-corp.com.\n\n"
    "Best regards,\nThe IT E-Corp Team\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=56, seconds=3))

# Set the parameter for the functions
container = elliotalderson_attacker
receiver = f"{sarahwilliams_email} {sampointer_email} {emilycarter_email} {oliviamurphy_email}"
sender = "elliotalderson"

# Attachment
attachment_path = "/usr/local/littleProject/dbUpdate.zip"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_with_attach(container, fake_date, receiver, email_subject, email_body, sender, attachment_path)

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
# Save attachment
print("\n---------- Save the zipped ransomware folder ----------")

container = sarahwilliams_computer1
user = "sarahwilliams"  

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=3, minutes=27, seconds=35))

set_fake_time(container, fake_date)
save_attachment_from_email(container, user)

time.sleep(5)

# Unzip folder
print("\n---------- Unzip the zipped ransomware folder ----------")

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=10, seconds=21))

container = sarahwilliams_computer1
user = "sarahwilliams"
folder_zip_name = "dbUpdate.zip"
target_zip = f"/home/{user}/downloads/{folder_zip_name}"
working_dir = f"/home/{user}"

set_fake_time(container, fake_date)
unzip_ransomware_folder(container, fake_date, user, target_zip, working_dir)

# Install the update
print("\n---------- Install the ransomware update ----------")

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=6, seconds=26))

container = sarahwilliams_computer1
user = "sarahwilliams"

set_fake_time(container, fake_date)
run_ransomware_script(container, user)

time.sleep(10)
