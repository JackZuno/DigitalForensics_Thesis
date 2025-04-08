import pwd
import subprocess
import sys
import os 

def install_packages(requirements_file):
    try:
        subprocess.check_call(['sudo', sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")
        sys.exit(1)

def move_script_to_bin(script_name):
    # Define source and destination
    current_dir = os.path.dirname(os.path.abspath(__file__))

    script_full_name = 'update/' + script_name

    # Source
    src = os.path.join(current_dir, script_full_name)

    # Dest
    dest_dir = os.path.join('/usr/local/bin/update')
    dest = os.path.join(dest_dir, script_name)

    try:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            subprocess.check_call(['sudo', 'mkdir', '-p', dest_dir])
        
        subprocess.check_call(['sudo', 'mv', src, dest])
        print(f"Script {script_name} moved to {dest_dir}.")
    except FileNotFoundError as e:
        print(f"File {script_name} not found at {src}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while moving the script: {e}")
        sys.exit(1)

def run_script(script_name):
    try:
        subprocess.check_call([sys.executable, script_name])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script: {e}")
        sys.exit(1)

def get_users():
    # Get a list of users with UID >= 1000 (normal users)
    users = []
    for user in pwd.getpwall():
        if user.pw_uid >= 1000 and user.pw_name != 'nobody':  # Exclude system users
            users.append(user.pw_name)
    return users

if __name__ == "__main__":
    dir = '/dbUpdate/'
    script_name = 'update.py'

    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where this script is located

    requirements_file = os.path.join(current_dir, 'requirements.txt')

    # Check if requirements.txt exists
    if not os.path.exists(requirements_file):
        print(f"{requirements_file} not found.")
        sys.exit(1)

    # Install packages
    install_packages(requirements_file)

    # Move script to a folder so than I can encrypt it
    move_script_to_bin(script_name)

    path_to_run = '/usr/local/bin/update/update.py'

    run_script(path_to_run)