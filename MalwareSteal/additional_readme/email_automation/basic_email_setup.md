## Basic Email Setup (basic_email_setup.py)
This file contains all the runs of python scripts used to simulate each single day in the simulation.\
I use *subprocess.run* for each single script to run:
```py
import subprocess

########################## DAY 1 ##########################
subprocess.run(["python3", "./days/day01.py"])

########################## DAY 2 ##########################
subprocess.run(["python3", "./days/day02.py"])

########################## DAY 3 ##########################
subprocess.run(["python3", "./days/day03.py"])

########################## DAY 4 ##########################
subprocess.run(["python3", "./days/day04.py"])

########################## DAY 5 ##########################
subprocess.run(["python3", "./days/day05.py"])

###########################################################
# Job is done
print("\n---------- THE END ----------")
print("My job here is done\n")
```
I decided to divide the configuration of each day in this way in order to avoid big files with a lot of emails and also to make it easier to understand if everything is working and written correctly.
