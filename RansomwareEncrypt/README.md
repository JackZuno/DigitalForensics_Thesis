## Ransomware Attack (Encryption)
### Architecture
This is the starting configuration that can be used to simulate attacks towards a company. \
It contains an external attacker who can communicate with workers via e-mails. \
To get more information about the structure and users that are part of the configuration look at the **[architecture](additional_readme/architecture.md)** file.

### How to Run It
To run the whole project in docker, you need to follow these steps:
```bash
# Inside the folder where the docker-compose.yml file is placed
docker-compose up --build
```
To stop the whole project in docker, you need to follow these steps:
```bash
# Inside the folder where the docker-compose.yml file is placed
docker-compose down --volumes --remove-orphans

# If you want to remove the images
docker system prune -a
```
To check if everything is running and to interact with the containers, you need to follow these steps:
```bash
# To see if everything is up and running
docker ps -a

# To interact with a specific container
# The command can be 'bash', to open the bash console of the container
# or it can be a specific bash command to run
docker exec -it container_id command

# Another example
docker exec -it container_name bash
```

### How to Extract the Image of a Container
Container images are useful for performing digital forensics, with tools such as *Autopsy*. It is possible to extract images of the container by using docker commands:
```bash
# Get the list of containers
docker ps -a

docker commit container_id commit_name
docker save -o C:\path\to\file\image_name_fs.tar commit_name

# Extract the .tar
# Open blobs
# Add into Autopsy the folder sha256
# Run ingest modules
```
When I was trying to analyze an image in Autopsy, I noticed that I had problems retrieving the information about the browser. I found out that I was able to obtain this information after the second run of the ingest modules, so I understood that the problem was that in the first run the data was not extracted, while in the second one Autopsy was able to retrieve the information.\
So, a solution that I found is this:
- First run with only *Embedded File Extractor*
- Second run with the other ingest modules 

To see more about this go here: **[autopsy](additional_readme/autopsy/autopsy.md)**.

### Setup
#### Email Server
In this configuration there is a local email server created to allow the exchange of emails between employees and also with people outside the company. \
To create the email server, I used **Postfix** and **Dovecot** for handling sending/receiving/storing emails, and mutt for the client side.\
For more information about the email server and how I setup Postfix and Dovecot go here: **[email_server](additional_readme/email_server.md)**.

#### Database Server
The database server is used to simulate a server of a company. In my case it contains some data about projects and other stuff work related. \
There are some account created, so a user will need username and password to access the database and retrieve some data. \
For more information about the database server go here: **[database_server](additional_readme/database_server.md)**.

#### Default Email Conversation
In order to create a fake conversation between the workers, I made a python script that I used to send and reply to emails. \
In this script I choose also the date and time of when the email is sent, so that I can create a more realistic environment.\
To see more about it, go here: **[email automation](additional_readme/email_automation.md)**.

#### Web Navigation With Selenium
To make it look like the users are navigating on the internet (in my case I did it only for computer1 with sarahwilliams), I created a python script named **start_web_nav** that visits web sites on the internet, downloads pdf and searches stuff on google. Every activity is done after setting a fake date, so that all searches are not close to each other.\
To know more about the script go here: **[web navigation with selenium](additional_readme/web_navigation.md)**.

#### Ransomware
In this configuration the ransomware targets some victim's folders and encrypt them. \
The folders that are targeted by the ransomware comprehend also the one where the script is placed, so it makes more difficult to understand the content of the script used to perform the attack. \
The attacker sends via email a *.zip* saying that it contains an important update to install with the instructions to follow. The victims extract the zip folder and run:
```bash
python3 dbUpdate/installer.py
```
This code will install the packages needed to run the script and it will run the *update.py* code that will contain the attack. \
To see more information about the ransomware go here: **[ransomware](additional_readme/ransomware.md)**.

#### Attack Automation
To automate the attack process, I used the same method as the one used for the **email default conversation**.\
I created a python script used to run a series of command inside a specific docker container in order to create the malicious zip folder from the attacker side, then send this zip to the victims via email. From the email side I run a script to save the attachment from the received email and then execute the script.\
To see more information about the automation of the ransomware attack go here: **[attack automation](additional_readme/attack_automation.md)**.

### Problems
Problems that I had during the setup: **[problems](additional_readme/problems.md)**.

### TODO: To Conduct a Simulation
Before running everything check the **initial_fake_date** inside the *write_emails.py* file; inside the *start_web_nav.py* file the fake date is managed differently: it starts from the current day and then from there the fake date is obtained by adding or removing a delta time.
- **docker-compose up --build**: to run the whole configuration and setup everything (devices, email server, database server with the content inside, etc)
- **python3 automation_emails/basic_email_setup.py**: this scrip is used to recreate a conversation between workers by using emails. Everything is done under a fake date, starting from a *initial_fake_date* set in the *write_emails.py* file
- **start_web_nav.py**: run this script on the container *computer1* in order to simulate and than to have a web history. This script should also save a wireshark capture that can be useful for having a clean network traffic capture
- **capture_traffic.py**: run this script inside the specific container to start the *wireshark capture* on both the *email server* and the *database server*. Additionally you can add the same script to other containers and capture the traffic also there
- **additional_setup.py**: run this script to reproduce the data breach. This script will add more emails, including those that are used for the ransomware attack and it also contains the calls to the database performed by the workers
