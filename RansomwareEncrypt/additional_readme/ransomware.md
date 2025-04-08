## Ransomware
### Installer File 
This script starts by installing the required packages from the *requirements.txt* file and then it moves the *update.py* script to the */usr/local/bin/update/* folder, so when the *update.py* script will be run the script itself get encrypted with all the other files. \
Then *update.py* is run.

### Update File
This script has different target directories and one of them is the directory where the script itself is placed. In this way the script will be encrypted right after it is run. \
Then for every target directory the code search for files to encrypt and then leaves in the principal directory a ransom note where it asks for payment.
