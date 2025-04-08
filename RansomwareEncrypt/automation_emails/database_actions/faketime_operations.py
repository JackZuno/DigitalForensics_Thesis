import subprocess
import os

# Credentials
username_db = "sampointer"
password_db = "sam"

database_server_container = "database_server"

# Tables
project_info_table = "project_info"
budget_info_table = "budget_info"
contact_information_table = "contact_information"
key_measurements_table = "key_measurements"
locations_table = "locations"
team_involved_table = "team_involved"

def query_fakedate(container, fake_date, username, password, table_name, database_name, query, user):
    print(f"Query from {username} on container {container} with fake date: {fake_date}...")

    destination_dir = f"home/{user}/personalStuff"
    output_csv_filename = f"{table_name}.csv"

    if not os.path.exists(destination_dir):
        command = f"sudo -u {user} mkdir -p {destination_dir}"

        subprocess.run(["docker", "exec", container, "bash", "-c", command])
        print(f"Folder '{destination_dir}' created.")
    else:
        print(f"Folder '{destination_dir}' already exists.")

    command = (
        f"sudo -u {user} faketime '{fake_date}' sh -c "
        f"'PGPASSWORD='{password}' psql -h {database_server_container} -d {database_name} -U {username} "
        f"--csv -c \"{query}\" > /{destination_dir}/{output_csv_filename}' &&"
        f"faketime '{fake_date}' touch /{destination_dir}/{output_csv_filename}"
    )

    subprocess.run(["docker", "exec", container, "bash", "-c", command])

def merge_files(container, user, input_folder, dest_folder, output_filename):
    if not os.path.exists(dest_folder):
        command = f"sudo -u {user} mkdir -p {dest_folder}"

        subprocess.run(["docker", "exec", container, "bash", "-c", command])
        print(f"Folder '{dest_folder}' created.")
    else:
        print(f"Folder '{dest_folder}' already exists.")

    # List CSV files in the input folder
    list_command = f"ls {input_folder}/*.csv"
    csv_files = subprocess.run(
        ["docker", "exec", container, "bash", "-c", list_command],
        capture_output=True,
        text=True
    )

    csv_files_list = csv_files.stdout.strip().split('\n')

    output_file_path = f"{dest_folder}/{output_filename}"

    merge_command = f"echo '' > {output_file_path}; "  

    for csv_file in csv_files_list:
        filename = os.path.basename(csv_file)
        
        # Add the filename as a header to the merge command
        merge_command += f"echo '{filename}' >> {output_file_path}; "
        
        # Append the contents of the CSV file to the output file
        merge_command += f"cat {csv_file} >> {output_file_path}; echo '' >> {output_file_path}; " 

    result = subprocess.run(
        ["docker", "exec", container, "bash", "-c", merge_command],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error merging CSV files: {result.stderr}")
    else:
        print(f"CSV files merged successfully into '{output_file_path}'.")

def insert_data(container, fake_date, username, password, table_name, database_name, user, section, detail, sub_detail):
    print(f"Inserting data into {table_name} from {username} on container {container} with fake date: {fake_date}...")

    query = f"INSERT INTO {table_name} (section, detail, sub_detail) VALUES ('{section}', '{detail}', '{sub_detail}');"

    command = (
        f"sudo -u {user} faketime '{fake_date}' bash -c "
        f"\"PGPASSWORD='{password}' psql -h database_server -d {database_name} -U {username} <<EOF\n"
        f"{query}\n"
        f"EOF\""
    )

    result = subprocess.run(["docker", "exec", container, "bash", "-c", command], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Data inserted successfully.")
    else:
        print(f"Failed to insert data: {result.stderr}")

def retrieve_data(container, fake_date, username, password, table_name, database_name, user):
    print(f"Inserting data into {table_name} from {username} on container {container} with fake date: {fake_date}...")

    query = f"SELECT * FROM {table_name};"

    command = (
        f"sudo -u {user} faketime '{fake_date}' bash -c "
        f"\"PGPASSWORD='{password}' psql -h database_server -d {database_name} -U {username} <<EOF\n"
        f"{query}\n"
        f"EOF\""
    )

    subprocess.run(["docker", "exec", container, "bash", "-c", command])
