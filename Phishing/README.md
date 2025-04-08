## Phishing
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

#### GoPhish
To simulate a phishing attack I used GoPhish that allows me to create a phishing campaign. \
In GoPhish it is possible to create a **sending profile** from which the server will send the emails to the victims, a landing page to fake a website, and a specific email. \
To see more about the setup of gophish go here: **[gophish](additional_readme/gophish.md)**.

#### Web Navigation With Selenium
To make it look like the users are navigating on the internet (in my case I did it only for computer1 with sarahwilliams), I created a python script named **start_web_nav** that visits web sites on the internet, downloads pdf and searches stuff on google. Every activity is done after setting a fake date, so that all searches are not close to each other.\
To know more about the script go here: **[web navigation with selenium](additional_readme/web_navigation.md)**.

### Problems
Problems that I had during the setup: **[problems](additional_readme/problems.md)**.

### TODO: To Conduct a Simulation
Before running everything check the **initial_fake_date** inside the *write_emails.py* file; inside the *start_web_nav.py* file the fake date is managed differently: it starts from the current day and then from there the fake date is obtained by adding or removing a delta time.
- **docker-compose up --build**: to run the whole configuration and setup everything (devices, email server, database server with the content inside, etc)
- **python3 automation_emails/basic_email_setup.py**: this scrip is used to recreate a conversation between workers by using emails. Everything is done under a fake date, starting from a *initial_fake_date* set in the *write_emails.py* file
- **start_web_nav.py**: run this script on the container *computer1* in order to simulate and than to have a web history. This script should also save a wireshark capture that can be useful for having a clean network traffic capture
- **capture_traffic.py**: run this script inside the specific container to start the *wireshark capture* on both the *email server* and the *database server*. Additionally you can add the same script to other containers and capture the traffic also there
- **GoPhish Campaign**: create and start a phishing campaing with gophish
- **get_scammed.py**: run this on the victims container to look for the phishing emails and get scammed (open the email, look for a website, insert the data inside a form and press enter)
- **additional_setup.py**: run this script to reproduce the attacker comportament after the attack. This script will add more emails, and it also contains the calls to the database performed by the workers and then the attacke, after the phishing campaign.
