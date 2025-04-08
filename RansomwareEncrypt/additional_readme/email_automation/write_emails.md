## Write Emails (write_emails.py)
This file contains all the functions used in the automation process and all the parameteres needed to create the fake conversations (like containers name, email addresses and the initial fake date).

### Parameters
An important parameter is the **initial_fake_date**, because I use this to set the starting date for the conversations. \
The fake_date, for the first day and first email, correspond to the initial_fake_date, then is incremented by hours/minutes/seconds.\
I set the **initial_fake_date** here so that it is the same for all the days and I can modify all dates by changing this one.\
For each user, I have two variables:
```py
sarahwilliams_computer1 = "computer1"
sarahwilliams_email = "sarahwilliams@e-corp.com"
```
The first one contains the name of the container, the second one the email address to use.

### set_fake_time
The **set_fake_time** function is used to temporary change the date on the *email_server*, that will last for a few seconds. In this way I am able to manage the dates when the email are sent.
```py
# Container in this case in "email_server"
subprocess.run(["docker", "exec", container, "sudo", "date", "--set", fake_date])
```

### send_email
The **send_email** function is use to send emails from a specific container (and user) to another user.
```py
command = f"echo '{body}' | sudo -u {user} faketime '{fake_date}' mutt -s '{subject}' {recipient}"
subprocess.run(["docker", "exec", container, "bash", "-c", command])
```
In the command I specify the user from which I want to use mutt and then I also use *faketime*, with the same fake time I use in the server, so I can choose a specific date and time to send the email.\
In the command I specify the *body*, the *subject* and the *recipient*.

### save_email
The **save_email** function is used to run a python script stored in the container itself needed to save in the *inbox* file the emails (this script is also run with crontab, but I use this function to make sure that the inbox is updated).\
In case there are any problem to login with dovecot, due to the changes of the date and time, I restart the dovecot and postfix server and try again to run the script.

### extract_message_id
The **extract_message_id** function is used to extract the Message-ID directly from the file in the container where I store the email to which I want to reply.\
The command run to perform this operation is:
```py
command = "grep 'Message-ID:' /tmp/original_email.txt | sed 's/Message-ID: //;s/<//;s/>//'"
result = subprocess.run(["docker", "exec", container, "bash", "-c", command], capture_output=True, text=True)
```
The **grep** command will extract from the file the *Message-ID*, while the **sed** command will extract from this line only the part between the "<>".

### send_email_reply
The **send_email_reply** functions is the one used to answer to an email. \
If you are answering to an email sent, the *first* variable must be set to *True*, because it means that the subject used in this case is without "Re: ", while if you are responding to a response the *first* variable must be set to false and the "Re: " prefix must be kept. \
The next thing is the **grep** command:
```py
grep_command = (
        f"grep -A 100 -B 10 '" + search_subject_final + "' /home/" + user + "/inbox | awk '/^From [^<]+ <[^>]+> ./ && NR!=1{exit} {print}' > /tmp/original_email.txt"
    )
```
This command search in the user inbox an email with the specified subject and use the variable "*-A* and *-B* to set how many lines must be extracted with the grep command (A stands for after the match, B stands for before the match).\
The **awk** command is then use to limit the grep until it finds another email. In this case, no matter how much is the number referring to "*-A*", the grep command will only show one email, because in the awk command I specify the start format of an email.\
Then I check if the email exists and extract the content of it. From the original email I need the **header** (for the information like the original sender and the date and time) and then the **cleaned body** (for including it in the response). The cleaned body is only the text of the original email, that will be part of the response with before it a sentence telling when and by whom the message was sent.\
Then, I am able to create the body for the response with this command:
```py
# The quoted_email is the body of the original email with each line preceded
# by >
full_body = f"{top_phrase}{quoted_email}\n\n{body}"
```
In the end, I clean the subject, so I do not have situations with double Re, like "Re: Re: " and then I create the reply command.
```py
reply_command = (
    f"echo -e '{full_body}' | "
    f"sudo -u {user} faketime '{fake_date}' mutt -e 'set edit_headers=yes' "
    f"-s 'Re: {cleaned_subject}' "
    f"-e 'my_hdr In-Reply-To: <{original_message_id}>' "
    f"{email_original_sender}"
)
subprocess.run(["docker", "exec", container, "bash", "-c", f"{reply_command}"])
```
In this case, **faketime '{fake_date}'** is used to start mutt with a specific date and time.

### remove_re_prefix
The **remove_re_prefix** function is used to remove the "Re: " prefix from the subject of the email. This can be used at the beginning or at the end of the **send_email_replay** function, in order to search with correct version of the subject or to add the clean version of the subject to command to send the reply.

### separate_name_email
The **separate_name_email** function is used to extract the name and email of the original sender of the email from a received email to which you want to respond.\
The name and email are extract from the *"From:"* field:
```
From: Sarah Williams <sarahwilliams@e-corp.com>
```

### zip_ransomware_folder
The **zip_ransomware_folder** functions is used to zip the folder that contains the fake update, used by the attacker to to trick the victims.
```py
command = f"cd {working_dir} && zip -r {zip_name} {target_folder}"

subprocess.run(["docker", "exec", container, "bash", "-c", command])
```

### unzip_ransomware_folder
The **unzip_ransomware_folder** function is used, from the victim prospective, to unzip the zipped folder received via email.
```py
command = f"cd {working_dir} && sudo -u {user} faketime '{fake_date}' unzip {target_zip}"

subprocess.run(["docker", "exec", container, "bash", "-c", command])
```

### save_attachment_from_email
The **save_attachment_from_email** function run a python script (*save_attachments.py*) that is, for convenience, I put inside the container from the Dockerfile. This script look for an email with a given subject and then, if it is present, it saves the attachment to the download folder.
```py
command = f"sudo -u {user} python3 /usr/local/bin/save_attachments.py"

subprocess.run(["docker", "exec", container, "bash", "-c", command])
```

### run_ransomware_script
The **run_ransomware_script** function is used to run the **installer.py** script that is inside the extracted folder.
```py
command = f"sudo -u {user} python3 /home/{user}/dbUpdate/installer.py"

subprocess.run(["docker", "exec", container, "bash", "-c", command])
```
