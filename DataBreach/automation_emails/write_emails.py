import re
import subprocess
import time

# Container used and emails
sarahwilliams_computer1 = "computer1"
sarahwilliams_email = "sarahwilliams@e-corp.com"

johndoe_computer2 = "computer2"
johndoe_email = "johndoe@e-corp.com"

emilycarter_computer3  = "computer3"
emilycarter_email = "emilycarter@e-corp.com"

jamesfoster_computer4 = "computer4"
jamesfoster_email = "jamesfoster@e-corp.com"

sampointer_pc1 = "pc1"
sampointer_email = "sampointer@e-corp.com"

jakethompson_pc2 = "pc2"
jakethompson_email = "jakethompson@e-corp.com"

annamoore_pc3 = "pc3"
annamoore_email = "annamoore@e-corp.com"

oliviamurphy_pc4 = "pc4"
oliviamurphy_email = "oliviamurphy@e-corp.com"

elliotalderson_attacker = "attacker"
elliotalderson_email = "elliotalderson@mrrobot.com"

email_server_container = "email_server"

# Initial fake date as a string
initial_fake_date = "2024-10-19 09:03:23"

def set_fake_time(container, fake_date):
    print(f"Setting fake time on container {container} to {fake_date}...")
    subprocess.run(["docker", "exec", container, "sudo", "date", "--set", fake_date])

def send_email(container, fake_date, recipient, subject, body, user):
    print(f"Sending email from {user} on container {container} with fake date: {fake_date}...")

    command = f"echo '{body}' | sudo -u {user} faketime '{fake_date}' mutt -s '{subject}' {recipient}"
    subprocess.run(["docker", "exec", container, "bash", "-c", command])

    # command_history = f"mutt -s '{subject}' {recipient}"

    # # Append the command to the user's history file
    # history_command = f'echo "{command_history}" >> /home/{user}/.bash_history && history -a'
    # subprocess.run(["docker", "exec", container, "bash", "-c", history_command])

def send_email_with_attach(container, fake_date, recipient, subject, body, user, attachment_path):
    print(f"Sending email with attachment from {user} on container {container} with fake date: {fake_date}...")

    command = f"echo '{body}' | sudo -u {user} faketime '{fake_date}' mutt -s '{subject}' -a '{attachment_path}' -- {recipient}"
    subprocess.run(["docker", "exec", container, "bash", "-c", command])

def save_email(container, timeout=15, max_retries=3, delay_between_retries=5):
    print(f"Saving the emails on {container}...")

    command = "python3 /usr/local/bin/save_email.py"
    
    for attempt in range(max_retries):
        try:
            # Run the command with a timeout
            subprocess.run(["docker", "exec", container, "bash", "-c", command], timeout=timeout)
            print("Email saving completed successfully.")
            return  # Exit the function if the command was successful
        except subprocess.TimeoutExpired:
            print("Email saving script timed out. Restarting Dovecot and Postfix services...")

            # Restart Dovecot
            restart_dovecot_command = "service dovecot restart"
            subprocess.run(["docker", "exec", "email_server", "bash", "-c", restart_dovecot_command])
            
            # Restart Postfix
            restart_postfix_command = "service postfix restart"
            subprocess.run(["docker", "exec", "email_server", "bash", "-c", restart_postfix_command])

            print("Dovecot and Postfix services restarted due to script timeout.")
        
        # Wait before the next attempt
        print(f"Retrying in {delay_between_retries} seconds...")
        time.sleep(delay_between_retries)
    
    print("Maximum retry attempts reached. Email saving failed.")

def extract_message_id(container):
    # Run a command to extract the Message-ID directly from the file in the container
    command = "grep 'Message-ID:' /tmp/original_email.txt | sed 's/Message-ID: //;s/<//;s/>//'"
    
    result = subprocess.run(["docker", "exec", container, "bash", "-c", command], 
                            capture_output=True, text=True)
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()  # Return the extracted Message-ID
    return None

def send_email_reply(container, fake_date, body, user, search_subject, first = True):
    print(f"Replying to email on container {container} with fake date: {fake_date}...")

    search_subject_final = remove_re_prefix(search_subject) if first else search_subject

    # Create the grep command to extract the email
    # -A: Number of lines under the match
    # -B: Number of lines above the match
    grep_command = (
        f"grep -A 100 -B 10 '" + search_subject_final + "' /home/" + user + "/inbox | awk '/^From [^<]+ <[^>]+> ./ && NR!=1{exit} {print}' > /tmp/original_email.txt"
    )

    subprocess.run(["docker", "exec", container, "bash", "-c", f"{grep_command}"])

    email_exists = subprocess.run(
        ["docker", "exec", container, "bash", "-c", "if [ -s /tmp/original_email.txt ]; then echo 'true'; else echo 'false'; fi"],
        capture_output=True,
        text=True
    ).stdout.strip()

    if email_exists == "true":
        original_message_id = extract_message_id(container)

        original_email_content = subprocess.run(
            ["docker", "exec", container, "cat", "/tmp/original_email.txt"],
            capture_output=True,
            text=True
        ).stdout.strip()

        subprocess.run(["docker", "exec", container, "bash", "-c", "sudo rm tmp/original_email.txt"])

        original_lines = original_email_content.splitlines()

        header_end_index = next((i for i, line in enumerate(original_lines) if line == ""), None)

        if header_end_index is None or header_end_index == 0:
            print("No valid headers found.")
            return

        original_sender_line = next((line for line in original_lines if line.startswith("From:")), None)
        if original_sender_line is None:
            print("No sender information found.")
            return

        # Extract original sender information
        original_sender = re.search(r'From: (.+)', original_sender_line)
        original_sender = original_sender.group(1).strip() if original_sender else "Unknown Sender"

        name_original_sender, email_original_sender = separate_name_email(original_sender)

        # Extract original date information
        original_date_line = next((line for line in original_lines if line.startswith("Date:")), None)
        original_date = re.search(r'Date: (.+)', original_date_line)
        original_date = original_date.group(1).strip() if original_date else "Unknown Date"

        top_phrase = f"On {original_date}, {name_original_sender} wrote:\n"

        original_body = "\n".join(original_lines[header_end_index + 1:])
        
        # Remove any remaining headers from the previous conversation
        # Regex pattern to match common email headers
        header_pattern = re.compile(r"^(From:|To:|Subject:|Date:|Message-ID:|In-Reply-To:|MIME-Version:|Content-Type:|Content-Disposition:|Received:|Return-Path:|X-Original-To:|Delivered-To:|References:|Status:|X-Keywords:)", re.IGNORECASE)
        
        # Filter out lines that match the headers
        cleaned_body = "\n".join(line for line in original_body.splitlines() if not header_pattern.match(line))
        quoted_email = "\n".join(f"> {line}" for line in cleaned_body.splitlines())

        full_body = f"{top_phrase}{quoted_email}\n\n{body}"

        # Remove, if present, the "Re: " part
        cleaned_subject = remove_re_prefix(search_subject)

        reply_command = (
            f"echo -e '{full_body}' | "
            f"sudo -u {user} faketime '{fake_date}' mutt -e 'set edit_headers=yes' "
            f"-s 'Re: {cleaned_subject}' "
            f"-e 'my_hdr In-Reply-To: <{original_message_id}>' "
            f"{email_original_sender}"
        )
        subprocess.run(["docker", "exec", container, "bash", "-c", f"{reply_command}"])
        print("Reply sent successfully.\n")
    else:
        print(f"No email found with subject: '{search_subject_final}'\n")

def remove_re_prefix(subject):
    if subject.startswith("Re: "):
        # Remove "Re: " from the start of the string
        subject = subject[4:]  
    return subject.strip()  

def separate_name_email(name_email):
    pattern = r'^(?P<name>.+?)\s*<(?P<email>.+?)>$'
    
    match = re.match(pattern, name_email)
    if match:
        # Extract name and email from the match groups
        name = match.group('name').strip()  
        email = match.group('email').strip()  
        return name, email
    else:
        return None, None  # Return None if the pattern doesn't match
    
def delete_file_and_folder(container, user, target):
    command = f"sudo -u {user} rm -r /home/{user}/personalStuff/{target}"

    subprocess.run(["docker", "exec", container, "bash", "-c", command])
