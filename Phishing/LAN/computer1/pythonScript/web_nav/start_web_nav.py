import time
import os
import subprocess
from datetime import datetime, timedelta
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def set_fake_time(fake_date):
    print(f"Setting fake time  to {fake_date}...")
    subprocess.run(["sudo", "date", "--set", fake_date])

def start_capture(capture_file):    
    print(f"Starting network capture, saving to {capture_file}...")

    tshark_process = subprocess.Popen(
        ["tshark", "-w", capture_file],  # Capture packets to the specified file
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    return tshark_process

def stop_capture(tshark_process):
    print("Stopping network capture...")

    tshark_process.terminate()
    tshark_process.wait()

def navigate_web_page(options, url, website_name, fake_date):
    driver = webdriver.Firefox(options=options)

    try:
        print(f"Looking for {website_name}")
        set_fake_time(fake_date)
        
        driver.get(url)

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print(f"Successfully navigated to {url}")

    except Exception as e:
        print(f"An error occurred: {e}")
        subprocess.run(["date"])
    finally:
        driver.quit()
        print("Browser closed")

def accept_cookies(driver):
    # List of possible translations for the cookie acceptance button
    cookie_acceptance_texts = [
        "Accetta tutto",  # Italian
        "Accept all",     # English
        "Aceptar todo",   # Spanish
        "Accepter tout",  # French
        "Alle akzeptieren", # German
        "Akceptuj wszystkie", # Polish
        "Aceitar todos",  # Portuguese
        "Aceptar todas"   # Latin American Spanish
    ]
    
    cookie_accepted = False 

    for text in cookie_acceptance_texts:
        try:
            # Wait for the cookie acceptance button to be present
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//div[text()='{text}']"))
            )

            # Try to find the cookie acceptance button
            agree_button = driver.find_element(By.XPATH, f"//div[text()='{text}']")
            if agree_button.is_displayed():
                agree_button.click()
                print(f"Accepted cookies with text: '{text}'")
                cookie_accepted = True
                break  
        except Exception:
            continue 

    if not cookie_accepted:
        print("Cookie acceptance not required or failed in all languages.")

def search_with_google(options, search_subject):
    driver = webdriver.Firefox(options=options)

    try:
        # Perform a search on Google
        print("Opening google.com...")
        driver.get("https://www.google.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print(f"Current URL: {driver.current_url}")

        time.sleep(5)

        # Check if the cookie acceptance prompt is present and Accept it
        accept_cookies(driver)

        # Perform a search on Google
        print(f"Searching '{search_subject}'...")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_subject)
        search_box.send_keys(Keys.RETURN)
        print(f"Performed search for '{search_subject}'")

        time.sleep(10)

        # Click the first result
        print("Waiting to click on the first result...")
        first_result = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
        )
        first_result.click()
        print("Clicked on the first search result")
    finally:
        # Close the browser
        driver.quit()
        print("Browser closed")

def download_pdf_function(pdf_url, pdf_name, driver, download_dir, fake_date):
    print(f"Downloading pdf: {pdf_name}")

    # Set the fake date
    set_fake_time(fake_date)

    driver.execute_script(f"window.location.href='{pdf_url}';") 

    # Wait for the PDF download to complete
    timeout = 60  
    start_time = time.time()

    while True:
        current_time = time.time() - start_time

        # Check if the PDF is downloaded in the folder
        downloaded_files = os.listdir(download_dir)
        if pdf_name in downloaded_files:
            print(f"Downloaded in {current_time}")
            print(f"PDF downloaded: {downloaded_files}")
            break

        # Exit if we hit the timeout
        if time.time() - start_time > timeout:
            print(f"Cause of the timeout: {current_time}")
            print("PDF download timeout exceeded.")
            break

        time.sleep(1) 
    
    time.sleep(2) 
    downloaded_files = os.listdir(download_dir)
    print(f"Downloaded files: {downloaded_files}")

def download_pdf(options, download_dir, pdf_url, pdf_name, fake_date):
    driver = webdriver.Firefox(options=options)

    pdf_name = os.path.basename(urlparse(pdf_url).path)

    try:
        download_pdf_function(pdf_url, pdf_name, driver, download_dir, fake_date)
    finally:
        driver.quit()
        print("Browser closed")

#######################################################################à

if __name__ == "__main__":
    print("Inside the wireshark capture scritp!!!")

    # ---------------------- SETUP ----------------------
    profile_path = "/home/sarahwilliams/.mozilla/firefox/profiles/sarahwilliams"
    download_dir = "/home/sarahwilliams/downloads"  

    # Ensure the download directory exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Set up Firefox options
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("-profile")
    options.add_argument(profile_path)

    # Setting preferences for downloading files
    options.set_preference("browser.download.folderList", 2)  
    options.set_preference("browser.download.dir", download_dir)  
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")  
    options.set_preference("pdfjs.disabled", True)  

    options.set_preference("acceptInsecureCerts", True)
    options.set_preference("security.cert_pinning.enforcement_level", 0) 
    options.set_preference("security.tls.version.min", 1)
    options.set_preference("security.tls.version.max", 3)

    # Paths for keylog and capture files
    key_log_file = "/home/sarahwilliams/networkCapture/keylogfile.txt"
    capture_file = "/home/sarahwilliams/networkCapture/web_navigation/web_navigation.pcap"

    # Initial fake date as a string (I use today and then add or remove days/hours/minutes)
    now = datetime.now()
    now_around_nine_am = now.replace(hour=9, minute=4, second=3, microsecond=0)

    initial_fake_date = str(datetime.strptime(str(now_around_nine_am), "%Y-%m-%d %H:%M:%S"))

    print("Call the function to start the capture")
    tshark_process = start_capture(capture_file)

    time.sleep(5)

    # ---------------------- Fake Navigation ----------------------

    ###############################################################
    # ---------------------- Navigation with Faketime (Killed By Google) ----------------------
    url = "https://killedbygoogle.com"
    website_name = "Killed By Google"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(days=1, hours=1, minutes=33, seconds=43))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and perform the search
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (Elliot Alderson) ----------------------
    url = "https://mrrobot.fandom.com/wiki/Elliot_Alderson"
    website_name = "Elliot Alderson"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj - timedelta(days=1, hours=1, minutes=33, seconds=43))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Searching Today Weather on google ----------------------
    search_subject = "Today Weather"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(hours=6, minutes=33, seconds=43))

    print(f"\nSearching {search_subject} on google on the {fake_date}...")

    # Set the fake date on the device
    set_fake_time(fake_date)

    # Perform a search on internet with google (original date and time)
    search_with_google(options, search_subject)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (E-Corp) ----------------------
    url = "https://mrrobot.fandom.com/wiki/E-Corp"
    website_name = "E-Corp"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(days=1, hours=5, minutes=2, seconds=43))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Download PDF with Faketime (sample.pdf) ----------------------
    pdf_url = "https://icseindia.org/document/sample.pdf"
    pdf_name = "sample.pdf"

    print("\n")

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj - timedelta(days=1, hours=10, minutes=33, seconds=43))

    # Set the fake date on the device and download the pdf
    download_pdf(options, download_dir, pdf_url, pdf_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (Example) ----------------------
    url = "https://www.example.com"
    website_name = "Example"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(days=2, hours=1, minutes=33, seconds=43))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (YouTube) ----------------------
    url = "https://www.youtube.com"
    website_name = "YouTube"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj - timedelta(hours=12, minutes=26, seconds=22))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (Data Breach Response) ----------------------
    url = "https://www.ftc.gov/business-guidance/resources/data-breach-response-guide-business"
    website_name = "Data Breach Response"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj - timedelta(hours=17, minutes=13, seconds=29))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Download PDF with Faketime (dummy.pdf) ----------------------
    pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    pdf_name = "dummy.pdf"

    print("\n")

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(days=3, hours=1, minutes=33, seconds=43))

    # Set the fake date on the device and download the pdf
    download_pdf(options, download_dir, pdf_url, pdf_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Searching 'Homes in Los Angeles' on google ----------------------
    search_subject = "Homes in Los Angeles"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(hours=7, minutes=17, seconds=13))

    print(f"\nSearching {search_subject} on google on the {fake_date}...")

    # Set the fake date on the device
    set_fake_time(fake_date)

    # Perform a search on internet with google (original date and time)
    search_with_google(options, search_subject)

    time.sleep(10)

    ###############################################################
    # ---------------------- Download PDF with Faketime (building_project.pdf) ----------------------
    pdf_url = "https://www.irbnet.de/daten/iconda/CIB19103.pdf"
    pdf_name = "building_project.pdf"

    print("\n")

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(days=4, hours=1, minutes=33, seconds=43))

    # Set the fake date on the device and download the pdf
    download_pdf(options, download_dir, pdf_url, pdf_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Download PDF with Faketime (some_report.pdf) ----------------------
    pdf_url = "https://cordis.europa.eu/docs/results/234127/final1-stadium-final-report.pdf"
    pdf_name = "some_report.pdf"

    print("\n")

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(days=3, hours=3, minutes=13, seconds=3))

    # Set the fake date on the device and download the pdf
    download_pdf(options, download_dir, pdf_url, pdf_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Download PDF with Faketime (technical_regulations_f1.pdf) ----------------------
    pdf_url = "https://www.fia.com/sites/default/files/fia_2024_formula_1_technical_regulations_-_issue_1_-_2023-04-25.pdf"
    pdf_name = "technical_regulations_f1.pdf"

    print("\n")

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(days=5, hours=2, minutes=23, seconds=23))

    # Set the fake date on the device and download the pdf
    download_pdf(options, download_dir, pdf_url, pdf_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Searching Best lawyers on google ----------------------
    search_subject = "Best lawyers"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj - timedelta(hours=3, minutes=33, seconds=43))

    print(f"\nSearching {search_subject} on google on the {fake_date}...")

    # Set the fake date on the device
    set_fake_time(fake_date)

    # Perform a search on internet with google (original date and time)
    search_with_google(options, search_subject)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (Amazon) ----------------------
    url = "https://www.amazon.it"
    website_name = "Amazon"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj - timedelta(days=1, hours=5, minutes=3, seconds=43))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (From Microseconds to Date) ----------------------
    url = "https://www.epochconverter.com"
    website_name = "From Microseconds to Date"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj - timedelta(days=2, hours=5, minutes=3, seconds=43))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Searching Tickets ATP finals on google ----------------------
    search_subject = "Tickets ATP finals"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(hours=7, minutes=13, seconds=23))

    print(f"\nSearching {search_subject} on google on the {fake_date}...")

    # Set the fake date on the device
    set_fake_time(fake_date)

    # Perform a search on internet with google (original date and time)
    search_with_google(options, search_subject)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (Google Calendar) ----------------------
    url = "https://calendar.google.com/calendar/u/0/r/month?pli=1"
    website_name = "Google Calendar"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(days=4, hours=5, minutes=3, seconds=43))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (Google Calendar) ----------------------
    url = "https://calendar.google.com/calendar/u/0/r/month?pli=1"
    website_name = "Google Calendar"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj - timedelta(days=4, hours=5, minutes=33, seconds=43))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (Google Calendar) ----------------------
    url = "https://calendar.google.com/calendar/u/0/r/month?pli=1"
    website_name = "Google Calendar"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj - timedelta(days=3, hours=1, minutes=24, seconds=43))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (Google Calendar) ----------------------
    url = "https://calendar.google.com/calendar/u/0/r/month?pli=1"
    website_name = "Google Calendar"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(days=2, hours=11, minutes=12, seconds=23))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Navigation with Faketime (Lock Pick) ----------------------
    url = "https://www.ukbumpkeys.com/collections/lock-pick-sets"
    website_name = "Lock Pick"

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj + timedelta(days=1, hours=3, minutes=41, seconds=17))

    print(f"\nLooking for '{website_name}' on the {fake_date}")

    # Set the fake date on the device and visit the website
    navigate_web_page(options, url, website_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Download PDF with Faketime (data_breach_info.pdf) ----------------------
    pdf_url = "https://www.imperva.com/resources/whitepapers/More-Lessons-Learned-from-Analyzing-100-Data-Breaches_WP.pdf"
    pdf_name = "data_breach_info.pdf"

    print("\n")

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj - timedelta(hours=4, minutes=12, seconds=11))

    # Set the fake date on the device and download the pdf
    download_pdf(options, download_dir, pdf_url, pdf_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- Download PDF with Faketime (stadium.pdf) ----------------------
    pdf_url = "https://www.majowiecki.com/pdf/MJW-structures-portfolio.pdf"
    pdf_name = "stadium.pdf"

    print("\n")

    date_obj = datetime.strptime(initial_fake_date, "%Y-%m-%d %H:%M:%S")
    fake_date = str(date_obj - timedelta(hours=5, minutes=52, seconds=11))

    # Set the fake date on the device and download the pdf
    download_pdf(options, download_dir, pdf_url, pdf_name, fake_date)

    time.sleep(10)

    ###############################################################
    # ---------------------- The END ----------------------

    input("Press the ENTER key to stop the capture...")

    # Call the function to stop the capture
    print("Call the function to stop the capture")
    stop_capture(tshark_process)
