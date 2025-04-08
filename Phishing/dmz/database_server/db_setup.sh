# Create Database with postgres as the owner
su - postgres -c "psql -c \"CREATE DATABASE evil_corp;\""

######################### CREATE USERS #########################

############ Sarah WIlliams ############
# Create user sarahwilliams (who will be granted access to modify data later)
su - postgres -c "psql -c \"CREATE USER sarahwilliams WITH PASSWORD 'sarah';\""

# Allow the user sarahwilliams to connect to the evil_corp database
su - postgres -c "psql -c \"GRANT CONNECT ON DATABASE evil_corp TO sarahwilliams;\""

# Grant all privileges to schema public (so user can see and access tables)
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE ON SCHEMA public TO sarahwilliams;\""

############ John Doe ############
su - postgres -c "psql -c \"CREATE USER johndoe WITH PASSWORD 'john';\""
su - postgres -c "psql -c \"GRANT CONNECT ON DATABASE evil_corp TO johndoe;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE ON SCHEMA public TO johndoe;\""

############ Sam Pointer ############
su - postgres -c "psql -c \"CREATE USER sampointer WITH PASSWORD 'sam';\""
su - postgres -c "psql -c \"GRANT CONNECT ON DATABASE evil_corp TO sampointer;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE ON SCHEMA public TO sampointer;\""

############ Emily Carter ############
su - postgres -c "psql -c \"CREATE USER emilycarter WITH PASSWORD 'emily';\""
su - postgres -c "psql -c \"GRANT CONNECT ON DATABASE evil_corp TO emilycarter;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE ON SCHEMA public TO emilycarter;\""

############ James Foster ############
su - postgres -c "psql -c \"CREATE USER jamesfoster WITH PASSWORD 'james';\""
su - postgres -c "psql -c \"GRANT CONNECT ON DATABASE evil_corp TO jamesfoster;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE ON SCHEMA public TO jamesfoster;\""

############ Jake Thompson ############
su - postgres -c "psql -c \"CREATE USER jakethompson WITH PASSWORD 'jake';\""
su - postgres -c "psql -c \"GRANT CONNECT ON DATABASE evil_corp TO jakethompson;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE ON SCHEMA public TO jakethompson;\""

############ Anna Moore ############
su - postgres -c "psql -c \"CREATE USER annamoore WITH PASSWORD 'anna';\""
su - postgres -c "psql -c \"GRANT CONNECT ON DATABASE evil_corp TO annamoore;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE ON SCHEMA public TO annamoore;\""

############ Olivia Murphy ############
su - postgres -c "psql -c \"CREATE USER oliviamurphy WITH PASSWORD 'olivia';\""
su - postgres -c "psql -c \"GRANT CONNECT ON DATABASE evil_corp TO oliviamurphy;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE ON SCHEMA public TO oliviamurphy;\""

######################### CREATE TABLES #########################

# Create the tables as the owner (postgres user)

# Create project_info table
su - postgres -c "psql -d evil_corp -c \"CREATE TABLE project_info (id SERIAL PRIMARY KEY, section VARCHAR(100), detail VARCHAR(100), sub_detail TEXT);\""

# Create budget_info table
su - postgres -c "psql -d evil_corp -c \"CREATE TABLE budget_info (id SERIAL PRIMARY KEY, section VARCHAR(100), detail VARCHAR(100), sub_detail TEXT);\""

# Create contact_information table
su - postgres -c "psql -d evil_corp -c \"CREATE TABLE contact_information (id SERIAL PRIMARY KEY, section VARCHAR(100), detail VARCHAR(100), sub_detail TEXT);\""

# Create key_measurements table
su - postgres -c "psql -d evil_corp -c \"CREATE TABLE key_measurements (id SERIAL PRIMARY KEY, section VARCHAR(100), detail VARCHAR(100), sub_detail TEXT);\""

# Create locations table
su - postgres -c "psql -d evil_corp -c \"CREATE TABLE locations (id SERIAL PRIMARY KEY, section VARCHAR(100), detail VARCHAR(100), sub_detail TEXT);\""

# Create team_involved table
su - postgres -c "psql -d evil_corp -c \"CREATE TABLE team_involved (id SERIAL PRIMARY KEY, section VARCHAR(100), detail VARCHAR(100), sub_detail TEXT);\""

######################### PRIVILEGES TO TABLES #########################

############ Sarah WIlliams ############
# Grant specific privileges (e.g., INSERT, UPDATE, DELETE) on the tables to sarahwilliams
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE project_info TO sarahwilliams;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE budget_info TO sarahwilliams;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE contact_information TO sarahwilliams;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE key_measurements TO sarahwilliams;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE locations TO sarahwilliams;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE team_involved TO sarahwilliams;\""

# Grant privileges on the sequences associated with the tables (needed for the COPY command)
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE project_info_id_seq TO sarahwilliams;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE budget_info_id_seq TO sarahwilliams;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE contact_information_id_seq TO sarahwilliams;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE key_measurements_id_seq TO sarahwilliams;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE locations_id_seq TO sarahwilliams;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE team_involved_id_seq TO sarahwilliams;\""

############ John Doe ############
# Grant specific privileges (e.g., INSERT, UPDATE, DELETE) on the tables to johndoe
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE project_info TO johndoe;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE budget_info TO johndoe;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE contact_information TO johndoe;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE key_measurements TO johndoe;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE locations TO johndoe;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE team_involved TO johndoe;\""

# Grant privileges on the sequences associated with the tables (needed for the COPY command)
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE project_info_id_seq TO johndoe;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE budget_info_id_seq TO johndoe;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE contact_information_id_seq TO johndoe;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE key_measurements_id_seq TO johndoe;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE locations_id_seq TO johndoe;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE team_involved_id_seq TO johndoe;\""

############ Sam Pointer ############
# Grant specific privileges (e.g., INSERT, UPDATE, DELETE) on the tables to sampointer
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE project_info TO sampointer;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE budget_info TO sampointer;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE contact_information TO sampointer;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE key_measurements TO sampointer;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE locations TO sampointer;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE team_involved TO sampointer;\""

# Grant privileges on the sequences associated with the tables (needed for the COPY command)
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE project_info_id_seq TO sampointer;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE budget_info_id_seq TO sampointer;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE contact_information_id_seq TO sampointer;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE key_measurements_id_seq TO sampointer;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE locations_id_seq TO sampointer;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE team_involved_id_seq TO sampointer;\""

############ Emily Carter ############
# Grant specific privileges (e.g., INSERT, UPDATE, DELETE) on the tables to emilycarter
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE project_info TO emilycarter;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE budget_info TO emilycarter;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE contact_information TO emilycarter;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE key_measurements TO emilycarter;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE locations TO emilycarter;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE team_involved TO emilycarter;\""

# Grant privileges on the sequences associated with the tables (needed for the COPY command)
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE project_info_id_seq TO emilycarter;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE budget_info_id_seq TO emilycarter;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE contact_information_id_seq TO emilycarter;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE key_measurements_id_seq TO emilycarter;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE locations_id_seq TO emilycarter;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE team_involved_id_seq TO emilycarter;\""

############ James Foster ############
# Grant specific privileges (e.g., INSERT, UPDATE, DELETE) on the tables to jamesfoster
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE project_info TO jamesfoster;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE budget_info TO jamesfoster;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE contact_information TO jamesfoster;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE key_measurements TO jamesfoster;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE locations TO jamesfoster;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE team_involved TO jamesfoster;\""

# Grant privileges on the sequences associated with the tables (needed for the COPY command)
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE project_info_id_seq TO jamesfoster;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE budget_info_id_seq TO jamesfoster;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE contact_information_id_seq TO jamesfoster;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE key_measurements_id_seq TO jamesfoster;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE locations_id_seq TO jamesfoster;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE team_involved_id_seq TO jamesfoster;\""

############ Jake Thompson ############
# Grant specific privileges (e.g., INSERT, UPDATE, DELETE) on the tables to jakethompson
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE project_info TO jakethompson;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE budget_info TO jakethompson;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE contact_information TO jakethompson;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE key_measurements TO jakethompson;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE locations TO jakethompson;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE team_involved TO jakethompson;\""

# Grant privileges on the sequences associated with the tables (needed for the COPY command)
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE project_info_id_seq TO jakethompson;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE budget_info_id_seq TO jakethompson;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE contact_information_id_seq TO jakethompson;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE key_measurements_id_seq TO jakethompson;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE locations_id_seq TO jakethompson;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE team_involved_id_seq TO jakethompson;\""

############ Anna Moore ############
# Grant specific privileges (e.g., INSERT, UPDATE, DELETE) on the tables to annamoore
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE project_info TO annamoore;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE budget_info TO annamoore;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE contact_information TO annamoore;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE key_measurements TO annamoore;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE locations TO annamoore;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE team_involved TO annamoore;\""

# Grant privileges on the sequences associated with the tables (needed for the COPY command)
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE project_info_id_seq TO annamoore;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE budget_info_id_seq TO annamoore;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE contact_information_id_seq TO annamoore;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE key_measurements_id_seq TO annamoore;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE locations_id_seq TO annamoore;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE team_involved_id_seq TO annamoore;\""

############ Olivia Murphy ############
# Grant specific privileges (e.g., INSERT, UPDATE, DELETE) on the tables to oliviamurphy
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE project_info TO oliviamurphy;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE budget_info TO oliviamurphy;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE contact_information TO oliviamurphy;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE key_measurements TO oliviamurphy;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE locations TO oliviamurphy;\""
su - postgres -c "psql -d evil_corp -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE team_involved TO oliviamurphy;\""

# Grant privileges on the sequences associated with the tables (needed for the COPY command)
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE project_info_id_seq TO oliviamurphy;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE budget_info_id_seq TO oliviamurphy;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE contact_information_id_seq TO oliviamurphy;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE key_measurements_id_seq TO oliviamurphy;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE locations_id_seq TO oliviamurphy;\""
su - postgres -c "psql -d evil_corp -c \"GRANT USAGE, SELECT ON SEQUENCE team_involved_id_seq TO oliviamurphy;\""

######################### END #########################
