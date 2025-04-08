## DataBase Setup

### Setup Server
The first thing I did it was exposing the port 5432 on the database server in the docker-compose.yml file, which is the PostgreSQL port. \
Then I installed on the server the needed package:
```Dockerfile
# Install PostgreSQL and related packages
RUN apt-get install -y postgresql postgresql-contrib
```
Then I modified two files, **pg_hba.conf** and **postgresql.conf**:
```py
# Inside /etc/postgresql/16/main/pg_hba.conf
# I added the md5 part and allow the access from specific network
# PostgreSQL Client Authentication Configuration File
# ===================================================
# This file controls: which hosts are allowed to connect,
# how clients are authenticated, which PostgreSQL user names
# they can use, which databases they can access.

# Database administrative login by Unix domain socket
local   all             postgres                                peer

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     md5
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
# IPv6 local connections:
host    all             all             ::1/128                 md5
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     peer
host    replication     all             127.0.0.1/32            md5
host    replication     all             ::1/128                 md5

# Allow access from 10.20.0.0/24 network
host    all             all             10.20.0.0/24           md5

# Allow access from 10.30.0.0/24 network
host    all             all             10.30.0.0/24           md5
```
```py
# Inside /etc/postgresql/16/main/postgresql.conf
# I remove the comment from this line:
listen_addresses = '*'

# I set SSL off and commented anything related to it
ssl = off

# I modified the log format
log_line_prefix = '%m [%p]: [%l-1] user=%u,db=%d,client=%h '

# Remove the comment here:
log_statement = 'all'
```

In the next step I worked on the **server-config.sh** file:
```bash
# Initialize PostgreSQL data directory (this happens on first run)
# This part check if the folder already exists and if not it will
# initialize it
PGDATA="/var/lib/postgresql/data"
if [ ! -d "$PGDATA" ]; then
    echo "Initializing PostgreSQL data directory..."
    su - postgres -c "/usr/lib/postgresql/$(pg_lsclusters -h | awk '{print $1}')/bin/initdb -D $PGDATA"
fi
```
Then I start the PostgreSQL service:
```bash
service postgresql start
```

### SSL/TLS
I enabled SSL/TLS with this changes on the **postgresql.conf** file:
```py
ssl = on
ssl_cert_file = '/etc/ssl/certs/ssl-cert-snakeoil.pem'
ssl_key_file = '/etc/ssl/private/ssl-cert-snakeoil.key'
```
I also modified the logs in the **postgresql.conf** file, so I can have more accurate logs:
```py
log_connections = on
log_disconnections = on
log_duration = on
log_hostname = on
log_line_prefix = '%m [%p]: user=%u, db=%d, client=%h '
```

### Create User and Database
The following steps are about the creation of the Database, users, set the permissions, tables, etc.
```bash
######################### CREATE DATABASE #########################
# Create Database
su - postgres -c "psql -c \"CREATE DATABASE evil_corp;\""

######################### CREATE USERS #########################
# Create user sarahwilliams (who will be granted access to modify data later)
su - postgres -c "psql -c \"CREATE USER sarahwilliams WITH PASSWORD 'sarah';\""

# Allow the user sarahwilliams to connect to the evil_corp database
su - postgres -c "psql -c \"GRANT CONNECT ON DATABASE evil_corp TO sarahwilliams;\""

# Grant all privileges to schema public (so user can see and access tables)
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE ON SCHEMA public TO sarahwilliams;\""

######################### CREATE TABLES #########################
# Create the tables as the owner (postgres user)
# Create project_info table
su - postgres -c "psql -d evil_corp -c \"CREATE TABLE project_info (id SERIAL PRIMARY KEY, section VARCHAR(100), detail VARCHAR(100), sub_detail TEXT);\""

######################### PRIVILEGES TO TABLES #########################
# Grant specific privileges (e.g., INSERT, UPDATE, DELETE) on the tables to sarahwilliams
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE project_info TO sarahwilliams;\""

# Grant privileges on the sequences associated with the tables (needed for the COPY command)
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE project_info_id_seq TO sarahwilliams;\""
```

### How to Interact with the Database from a Computer
On the computer side, you need to install:
```Dockerfile
# Install PostgreSQL client
RUN apt-get install -y postgresql-client
```
In order to let the computer know the ip address of database_server, this command is needed:
```bash
echo "192.168.1.2 database_server" >> /etc/hosts
```
To access the database from the computer, it is possible to use a command like that:
```bash
# Inside the commputer 

# It is important to use "-h database_server", so it know where the server is
PGPASSWORD='sarah' psql -h database_server -d evil_corp -U sarahwilliams
# Then insert the password

# One line command
PGPASSWORD='sarah' psql -h database_server -d evil_corp -U sarahwilliams
```
 and to perform some operations:
```bash
 # Retrieve some data
PGPASSWORD='sarah' psql -h database_server -d evil_corp -U sarahwilliams -c "SELECT * FROM project_info;"

# Copy some data from a file to a table
PGPASSWORD='sarah' psql -h database_server -d evil_corp -U sarahwilliams -c "\COPY project_info(section, detail, sub_detail) FROM './path/projectOverview.csv' DELIMITER ',' CSV HEADER;"
```

### How to Perform Operations On The Database

To perform some opeartions from the server using an user previously created:
```bash
# Inside the database server

# Create a table
PGPASSWORD='sarah' psql -d evil_corp -U sarahwilliams -c "CREATE TABLE project_info (id SERIAL PRIMARY KEY, name VARCHAR(100));"

# Insert something in the table
PGPASSWORD='sarah' psql -d evil_corp -U sarahwilliams -c "INSERT INTO project_info (name) VALUES ('Test Name 1'), ('Test Name 2');"

# Retrieve content table
PGPASSWORD='sarah' psql -d evil_corp -U sarahwilliams -c "SELECT * FROM project_info;"

# Copy the content from a CSV file to a table
PGPASSWORD='sarah' psql -d evil_corp -U sarahwilliams -c "\COPY project_info(section, detail, sub_detail) FROM './path/to/file/projectOverview.csv' DELIMITER ',' CSV HEADER;"
```
All these operations must be performed from the server, because in the command there is no server specified (missing *-h database_server*).
