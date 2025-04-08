## DataBase Server
The database server is used to simulate a server of a company. In my case it contains some data about projects and other stuff work related. \
There are some account created, so a user will need username and password to access the database and retrieve some data.\
To create the database server in my configuration I used PostgreSQL.

### Setup Server
To see how I setup the database server go here: **[database_setup](database_server/db_setup.md#database-setup)**.

### Create User and Database
THe users are created inside the **db_setup.sh** file, which is started in the **server-config.sh** file. \
When I create a new user, I choose a username, a password and I give the permissions needed to the user to perform operations on the database.\
Also, after the creation, the user must be allowed to connect to the database.
To see how the creation of new users is made go here: **[user_creation](database_server/db_setup.md#create-user-and-database)**.

### SSL/TLS
To see how to setup SSL/TLS in the database server go here: **[SSL/TLS](database_server/db_setup.md#ssltls)**.

### How to Interact with the Database from a Computer
In this case, the operations are performed from a computer, so the host must be specified, so the computer knows how to connect to the server. \
To see how to interact with the database server from a computer go here: **[interact with the db server from a computer](database_server/db_setup.md#how-to-interact-with-the-database-from-a-computer)**.

### How to Perform Opeartions On The Database
In this case, the operations are performed from the server, so no host must be specified. \
To see how to perform operations on the database server go here: **[operations on the db server](database_server/db_setup.md#how-to-perform-operations-on-the-database)**.

### View Database Logs
To see the **logs** of the database server, you need to go here:
```bash
# Static
cat /var/log/postgresql/postgresql-16-main.log

# Dynamic
tail -f /var/log/postgresql/postgresql-16-main.log
```
