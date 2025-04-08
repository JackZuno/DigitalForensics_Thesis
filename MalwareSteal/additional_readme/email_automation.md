## Email Automation
In order to create a fake conversation between the workers, I made a python script that I used to send and reply to emails. \
In this script I choose also the date and time of when the email is sent, so that I can create a more realistic environment.\
I divided the python script in different files: one for the functions and parameters, one for running the whole script and the others for each day I am simulating.

### Python Script
#### Write Emails (write_emails.py)
This file contains all the functions used in the automation process and all the parameteres needed to create the fake conversations (like containers name, email addresses and the initial fake date).\
To see more about the content of this file go here: **[write_emails.py](email_automation/write_emails.md)**.

#### Basic Email Setup (basic_email_setup.py)
This file contains all the runs of python scripts used to simulate each single day in the simulation.\
To see more about the content of this file go here: **[basic_email_setup.py](email_automation/basic_email_setup.md)**.

#### DayXX (dayXX.py)
This file is the one responsable for sending emails and replying to them, with the ending goal to create a fake conversation.
To see more about the content of this file go here: **[dayXX.py](email_automation/dayXX.md)**.
