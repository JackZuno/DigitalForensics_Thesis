import time
from write_emails import *
from datetime import datetime, timedelta
from database_actions.faketime_operations import *

########################## DAY 9 ##########################

print("\n-------------- DAY 9 (Phishing) --------------")

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
