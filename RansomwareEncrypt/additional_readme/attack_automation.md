## Attack Automation
To automate the attack process, I used the same method as the one used for the **email default conversation**.\
I created a python script used to run a series of command inside a specific docker container in order to create the malicious zip folder from the attacker side, then send this zip to the victims via email. From the email side I run a script to save the attachment from the received email and then execute the script.

### Python Script
#### Write Emails (write_emails.py)
This is the file where I added the functions needed for implementing the attack, like **zip_ransomware_folder**, **unzip_ransomware_folder**, **save_attachment_from_email** and **run_ransomware_script**.
This file originally contains all the functions used in the automation process and all the parameteres needed to create the fake conversations (like containers name, email addresses and the initial fake date).\
The functions that I added are not complex and just basics command, except for the one for saving the attachment that runs a python script from the container itself (it is a script that I put inside of it).\
To see more about the content of this file go here: **[write_emails.py](email_automation/write_emails.md)**.

#### Additional Setup (additional_setup.py)
This file contains all the runs of python scripts used to simulate each single day in the simulation.\
The content of the file is the same as the one in the **basic_email_setup**, so for more reference go to the documentation about it.s
To see more about the content of this file go here: **[basic_email_setup.py](email_automation/basic_email_setup.md)**.

#### DayXX (dayXX.py)
This file is the one responsable for sending emails and replying to them, with the ending goal to create a fake conversation and do some actions.\
The **dayXX** files used for the attack proccess are the same used for the default conversation setup.\
To see more about the content of this file go here: **[dayXX.py](email_automation/dayXX.md)**.
