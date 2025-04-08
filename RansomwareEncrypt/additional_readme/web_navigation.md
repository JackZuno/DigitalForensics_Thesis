## Web Navigation With Selenium
To make it look like the users are navigating on the internet (in my case I did it only for computer1 with sarahwilliams), I created a python script named **start_web_nav** that visits web sites on the internet, downloads pdf and searches stuff on google. Every activity is done after setting a fake date, so that all searches are not close to each other.\
In the first part of the script there are the function used to navigate on the internet:
- **start_capture**: This function starts the network capture using wireshark.
- **stop_capture**: This function stops the network capture using wireshark.
- **set_fake_time**: This function sets the time of the container (in this case the computer1) to a specific date and time
- **navigate_web_page**: This function starts the Firefox WebDriver and then inside a *try* it will set the fake date and then try to visit the website. After that, it closes the browser.
- **accept_cookies**: This function is needed when you perform searches using google, because it checks, in various languages, if there are google cookies to accept in order to keep going.
- **search_with_google**: This function goes to google.com and then from here it performs a search with google. After it insert the words to search, it waits and then clicks on the first result.
- **download_pdf_function**: This is the function used to download pdf files from the internet. It receives the pdf url, pdf name, download dir as parameter and then perfrom the download.
- **download_pdf**: This is the wrapper function that inside the try calls the *download_pdf_function*.

The functions are then followed by the main, where there is the set up of firefox (passing the firefox profile used, the download dir, etc) and then there are the calls to the functions to re-create a user internet navigation.

### Set Up
The first part of the main is dedicated to the setup of FireFox options:
```py
# Here there are the paths of the firefox profile used and the download directory
profile_path = "/home/sarahwilliams/.mozilla/firefox/profiles/sarahwilliams"
download_dir = "/home/sarahwilliams/downloads"  # Use absolute path

# Ensure the download directory exists
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Set up Firefox options
options = Options()
options.add_argument("--headless")  # Needed because there is no UI
options.add_argument("-profile")
options.add_argument(profile_path)

# Setting preferences for downloading files
options.set_preference("browser.download.folderList", 2)  # Use custom download directory
options.set_preference("browser.download.dir", download_dir)  # Set download directory
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")  # Auto-download PDF
options.set_preference("pdfjs.disabled", True)  # Disable built-in PDF viewer

# These four preferences are needed to make the web navigatin with fake date works
options.set_preference("acceptInsecureCerts", True)
options.set_preference("security.cert_pinning.enforcement_level", 0)  # Disable cert pinning
options.set_preference("security.tls.version.min", 1)
options.set_preference("security.tls.version.max", 3)
```
After that the keylogfile and wireshark capture files destination paths are defined:
```py
# Paths for keylog and capture files
key_log_file = "/home/sarahwilliams/networkCapture/keylogfile.txt"
capture_file = "/home/sarahwilliams/networkCapture/computer_capture.pcap"
```
The setup ends with the date used as starting point for creating the other dates used in the calls to the functions:
```py
# Initial fake date as a string (I use today and then add or remove days/hours/minutes)
now = datetime.now()
now_around_nine_am = now.replace(hour=9, minute=4, second=3, microsecond=0)

# This is the date from that I will use timedelta to change the value
initial_fake_date = str(datetime.strptime(str(now_around_nine_am), "%Y-%m-%d %H:%M:%S"))
```

### Example on How I Call the Functions
**Navigation with Faketime (Killed By Google)**:
```py
# ---------------------- Navigation with Faketime (Killed By Google) ----------------------
url = "https://killedbygoogle.com"
website_name = "Killed By Google"

date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=1, hours=1, minutes=33, seconds=43))

print(f"\nLooking for '{website_name}' on the {fake_date}")

# Set the fake date on the device and perform the search
navigate_web_page(options, url, website_name, fake_date)

time.sleep(10)
```

**Searching Selenium Webdriver on google**:
```py
# ---------------------- Searching Selenium Webdriver on google ----------------------
search_subject = "Selenium Webdriver"

date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(hours=6, minutes=33, seconds=43))

print(f"\nSearching {search_subject} on google on the {fake_date}...")

# Set the fake date on the device
set_fake_time(fake_date)

# Perform a search on internet with google (original date and time)
search_with_google(options, search_subject)

time.sleep(10)
```

**Download PDF with Faketime (dummy.pdf)**:
```py
# ---------------------- Download PDF with Faketime (dummy.pdf) ----------------------
pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
pdf_name = "dummy.pdf"

print("\n")

date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj + timedelta(days=3, hours=1, minutes=33, seconds=43))

# Set the fake date on the device and download the pdf
download_pdf(options, download_dir, pdf_url, pdf_name, fake_date)
```
When you use **timedelta**, it is possible to choose if you want to add or remove the amount of time specified inside the function.\ 
In the examples that I showed I am adding the delta to the *initial_fake_date* with the **+**, but if you want to go back in the past and remove that amount of time you just need to use the **-**, just like this:
```py
# ---------------------- Navigation with Faketime (Killed By Google) ----------------------
url = "https://killedbygoogle.com"
website_name = "Killed By Google"

date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
fake_date = str(date_obj - timedelta(days=1, hours=1, minutes=33, seconds=43))

print(f"\nLooking for '{website_name}' on the {fake_date}")

# Set the fake date on the device and perform the search
set_fake_time(fake_date)
navigate_web_page(options, url, website_name, fake_date)

time.sleep(10)
```

### Problems
When you are changing the date and time and then perform a web search, you must know that it can cause an error, due to security problems (most of the time related to the certificates).\
In this case I noticed that, if the website give you some problems when changing date and time, a solution could be to change the date, from the current one, by max 1 or 2 days.\
Erorr:
```py
Looking for 'E-Corp' on the 2024-10-28 13:44:32
Setting fake time  to 2024-10-28 13:44:32...
Mon Oct 28 13:44:32 UTC 2024
Looking for E-Corp
Setting fake time  to 2024-10-28 13:44:32...
Mon Oct 28 13:44:32 UTC 2024
An error occurred: Message: Reached error page: about:neterror?e=nssFailure2&u=https%3A//mrrobot.fandom.com/wiki/E-Corp&c=UTF-8&d=%20
Stacktrace:
RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8
WebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:193:5
UnknownError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:832:5
checkReadyState@chrome://remote/content/marionette/navigate.sys.mjs:58:24
onNavigation@chrome://remote/content/marionette/navigate.sys.mjs:343:39
emit@resource://gre/modules/EventEmitter.sys.mjs:148:20
receiveMessage@chrome://remote/content/marionette/actors/MarionetteEventsParent.sys.mjs:33:25
```
