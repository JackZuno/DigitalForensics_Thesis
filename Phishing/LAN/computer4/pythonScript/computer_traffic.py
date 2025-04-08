import time
import subprocess
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def start_capture(capture_file):    
    # Start capturing traffic with tshark
    print(f"Starting network capture, saving to {capture_file}...")

    tshark_process = subprocess.Popen(
        ["tshark", "-w", capture_file],  # Capture packets to the specified file
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    return tshark_process

def stop_capture(tshark_process):
    # Stop the tshark process and wait for it to finish
    print("Stopping network capture...")

    tshark_process.terminate()
    tshark_process.wait()

def download_pdf(pdf_url, pdf_name, driver, download_dir):
    print(f"Downloading pdf: {pdf_name}")

    driver.execute_script(f"window.location.href='{pdf_url}';")  # Use JS to initiate PDF download

    # Wait for the PDF download to complete
    timeout = 15  # Set a timeout for waiting for the download to complete
    start_time = time.time()

    while True:
        # Check if the PDF is downloaded in the folder
        downloaded_files = os.listdir(download_dir)
        if any(file.endswith(".pdf") for file in downloaded_files):
            print(f"PDF downloaded: {downloaded_files}")
            break

        # Exit if we hit the timeout
        if time.time() - start_time > timeout:
            print("PDF download timeout exceeded.")
            break

        time.sleep(1)  # Wait a little before checking again
    
    # Check if files have been downloaded
    time.sleep(2)  # Wait for the file to download
    downloaded_files = os.listdir(download_dir)
    print(f"Downloaded files: {downloaded_files}")

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
    
    cookie_accepted = False  # Flag to check if cookies were accepted

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
                break  # Exit the loop if cookies were accepted
        except Exception:
            continue  # Continue to the next translation if the current one fails

    if not cookie_accepted:
        print("Cookie acceptance not required or failed in all languages.")

def fake_traffic1(options, download_dir):
    print("######################################### FAKE TRAFFIC 1 #########################################")

    # Start the Firefox WebDriver
    driver = webdriver.Firefox(options=options)

    try:
        # Visit example.com
        print("Visiting example.com...")
        driver.get("https://www.example.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait until page loads
        print(f"Current URL: {driver.current_url}")

        time.sleep(6)

        # Perform a search on Google
        print("Visiting google.com...")
        driver.get("https://www.google.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print(f"Current URL: {driver.current_url}")

        time.sleep(5)

        # Check if the cookie acceptance prompt is present and Accept it
        accept_cookies(driver)

        # Perform a search on Google
        print("Searching 'Selenium WebDriver'...")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium WebDriver")
        search_box.send_keys(Keys.RETURN)
        print("Performed search for 'Selenium WebDriver'")

        time.sleep(10)

        # Click the first result
        print("Waiting to click on the first result...")
        first_result = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
        )
        first_result.click()
        print("Clicked on the first search result")

        time.sleep(9)

        # Download a pdf
        pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
        pdf_name = "dummy.pdf"
        download_pdf(pdf_url, pdf_name, driver, download_dir)

    finally:
        # Close the browser
        driver.quit()
        print("Browser closed")

def fake_traffic2(options, download_dir):
    print("######################################### FAKE TRAFFIC 2 #########################################")

    # Start the Firefox WebDriver
    driver = webdriver.Firefox(options=options)
    try:
        # Visit example.com
        print("Looking for a perfect data breach")
        driver.get("https://www.ekransystem.com/en/blog/data-breach-investigation-best-practices")

        time.sleep(6)

        # Visit e-corp
        print("Visiting evil-corp...")
        driver.get("https://mrrobot.fandom.com/wiki/E-Corp")

        time.sleep(4)

        # Download a pdf
        pdf_url = "https://digitalcommons.coastal.edu/cgi/viewcontent.cgi?article=1098&context=cbj"
        pdf_name = "info_db.pdf"
        download_pdf(pdf_url, pdf_name, driver, download_dir)

        time.sleep(11)

        # Perform a search on Google
        print("Visiting google.com...")
        driver.get("https://www.google.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print(f"Current URL: {driver.current_url}")

        time.sleep(10)

        # Check if the cookie acceptance prompt is present and Accept it
        accept_cookies(driver)
            
        # Perform a search on Google
        print("Searching 'Consequences of data breach'...")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Consequences of data breach")
        search_box.send_keys(Keys.RETURN)
        print("Performed search for 'Consequences of data breach'")

        time.sleep(7)

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

def fake_traffic3(options, download_dir):
    print("######################################### FAKE TRAFFIC 3 #########################################")

    # Start the Firefox WebDriver
    driver = webdriver.Firefox(options=options)
    try:
        # Download a pdf
        pdf_url = "https://www.irbnet.de/daten/iconda/CIB19103.pdf"
        pdf_name = "building_project.pdf"
        download_pdf(pdf_url, pdf_name, driver, download_dir)

        time.sleep(12)

        # Visit example.com
        print("Looking for killed by google")
        driver.get("https://killedbygoogle.com")

        time.sleep(5)

        # Visit e-corp
        print("Looking for Elliot Alderson...")
        driver.get("https://mrrobot.fandom.com/wiki/Elliot_Alderson")

        time.sleep(6)

        # Perform a search on Google
        print("Visiting google.com...")
        driver.get("https://www.google.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print(f"Current URL: {driver.current_url}")

        time.sleep(5)

        # Check if the cookie acceptance prompt is present and Accept it
        accept_cookies(driver)

        # Perform a search on Google
        print("Searching 'Best spots in italy'...")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Best spots in italy")
        search_box.send_keys(Keys.RETURN)
        print("Performed search for 'Best spots in italy'")

        time.sleep(7)

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

if __name__ == "__main__":
    print("Inside the wireshark capture scritp!!!")

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

    # Paths for keylog and capture files
    key_log_file = "/home/sarahwilliams/networkCapture/keylogfile.txt"
    capture_file = "/home/sarahwilliams/networkCapture/computer_capture.pcap"

    # Call the function to start the capture
    print("Call the function to start the capture")
    tshark_process = start_capture(capture_file)

    # # Wait 30 seconds
    time.sleep(5)

    # Fake traffic 1
    fake_traffic1(options, download_dir)

    # Wait five second
    time.sleep(5)

    # Fake traffic 2
    fake_traffic2(options, download_dir)

    time.sleep(9)

    # Fake traffic 3
    fake_traffic3(options, download_dir)

    time.sleep(7)

    input("Press the ENTER key to stop the capture...")

    # Call the function to stop the capture
    print("Call the function to stop the capture")
    stop_capture(tshark_process)
    