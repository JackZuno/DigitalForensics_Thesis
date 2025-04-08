import time
from write_emails import *
from datetime import datetime, timedelta

########################## DAY 5 ##########################

print("\n-------------- DAY 5 --------------")

# Select the fake date
date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=4, minutes=24, seconds=51))

print("Starting date DAY 5: ", fake_date, "\n")

###########################################################
# Send email (annamoore -> sarahwilliams)
print("\n---------- Send email (annamoore -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Client Proposal Revision"
email_body = (
    "Hi Sarah,\n"
    "I have just received feedback from one of our key clients about the proposal we sent last week.\n"
    "They are asking for some urgent revisions, especially regarding pricing and timeline estimates.\n"
    "I have started making the necessary changes, but can you review it and provide your input?\n"
    "I want to ensure we send back a polished version by tomorrow.\n\n"
    "Thanks,\nAnna\n"
)

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
# Reply email (sarahwilliams -> annamoore)
print("\n---------- Reply email (sarahwilliams -> annamoore) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Client Proposal Revision"
email_body = (
    "Hi Anna,\n\n"
    "Thanks for the heads-up. I will review the updated proposal this afternoon and provide any necessary revisions.\n"
    "Lets aim to have it finalized by end of day today so we have time for a quick quality check tomorrow before sending it to the client.\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=45, seconds=23))

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
# Send email (jamesfoster -> sarahwilliams)
print("\n---------- Send email (jamesfoster -> sarahwilliams) ----------")

# Set the email arguments
email_subject = "Request for Additional Resources"
email_body = (
    "Hi Sarah,\n"
    "I wanted to touch base regarding the current project timeline.\n"
    "After discussing with my team, it looks like we might need some additional resources to stay on track, especially in terms of technical support.\n"
    "Would it be possible to allocate some extra team members or bring in outside contractors for the next phase of the project?\n"
    "I understand there might be budget constraints, but any support would be helpful.\n\n"
    "Best,\nJames\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=4, seconds=25))

# Set the parameter for the functions
container = jamesfoster_computer4
receiver = sarahwilliams_email
sender = "jamesfoster"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email(container, fake_date, receiver, email_subject, email_body, sender)

# Sleep
time.sleep(5)

###########################################################
# Reply email (sarahwilliams -> jamesfoster)
print("\n---------- Reply email (sarahwilliams -> jamesfoster) ----------")

# Retrieve the email with sarahwilliams
save_email(sarahwilliams_computer1)

# Set the email arguments
email_subject = "Re: Request for Additional Resources"
email_body = (
    "Hi James,\n\n"
    "I understand the concern. I will look into whether we can allocate some additional resources internally, but if needed,\n"
    "we can consider bringing in contractors for a short period.\n"
    "Let me check with HR and finance, and I will get back to you by tomorrow with an update.\n\n"
    "Thanks for flagging this early, lets make sure we do not fall behind.\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=45, seconds=23))

# Set the parameter for the functions
container = sarahwilliams_computer1
receiver = jamesfoster_email
sender = "sarahwilliams"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)

###########################################################
# Send email (sarahwilliams -> johndoe)
print("\n---------- Send email (sarahwilliams -> johndoe) ----------")

# Set the email arguments
email_subject = "Project Status"
email_body = (
    "Hi John,\n"
    "Just checking in on the project timeline. Have we received the latest data from IT?\n"
    "I think it is crucial for our next steps.\n\n"
    "Let me know when you have a moment to chat.\n\n"
    "Best,\nSarah\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=25, seconds=25))

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
# Reply email (johndoe -> sarahwilliams)
print("\n---------- Reply email (johndoe -> sarahwilliams) ----------")

# Retrieve the email with johndoe
save_email(johndoe_computer2)

# Set the email arguments
email_subject = "Re: Project Status"
email_body = (
    "Hi Sarah,\n\n"
    "Yes, I got the updates this morning. There are some interesting trends we should discuss.\n"
    "I am free tomorrow after 5 PM if that works for you.\n\n"
    "Best,\nJohn\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(minutes=45, seconds=23))

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
# Reply email (jamesfoster -> sarahwilliams)
print("\n---------- Reply email (jamesfoster -> sarahwilliams) ----------")

# Retrieve the email with jamesfoster
save_email(jamesfoster_computer4)

# Set the email arguments
email_subject = "Re: Team Collaboration Meeting"
email_body = (
    "Hi Sarah,\n\n"
    "Sorry but I missed this. We can do it tomorrow morning, I had a lot of stuff to do!\n\n"
    "Talk soon,\nJames\n"
)

date_obj = datetime.strptime(fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=1, minutes=15, seconds=33))

# Set the parameter for the functions
container = jamesfoster_computer4
receiver = sarahwilliams_email
sender = "jamesfoster"

# Set fake time on the server and send the email
set_fake_time(email_server_container, fake_date)
send_email_reply(container, fake_date, email_body, sender, email_subject)

# Sleep
time.sleep(5)
