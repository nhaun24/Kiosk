import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import configparser
import sys
import tempfile

# wait for host to initialize. can change this timer
print("Please wait for host to initialize, do not exit from this screen")
time.sleep(1)

# Change directory to the specified path
os.chdir('/var/kiosk')

# Execute the Git pull command
os.system('git pull --no-verify https://github.com/nhaun24/Kiosk Linux')

# Start Xvfb
display = Display(visible=1, size=(1920, 1080))  # Adjust the size as needed
display.start()

# Path to the geckodriver executable
chromedriver_path = '/snap/bin/chrome'  # Update this line with the correct path

# Add geckodriver to the system's PATH
os.environ['PATH'] += os.pathsep + os.path.dirname(geckodriver_path)

# Create a temporary directory for the profile
temp_profile_dir = tempfile.mkdtemp()

# Create Firefox options
chrome_options = Options()
chrome_options.add_argument("--no-remote")
chrome_options.add_argument(f"--profile={temp_profile_dir}")
#chrome_options.binary_location = '/usr/bin/chrome'
#firefox_options.add_argument("--kiosk")
chrome_options.add_argument("--port=4445")
#firefox_options.add_argument("--headless")
#firefox_options.add_argument("--start-fullscreen")

# Specify the path to the ChromeDriver executable
chrome_service = ChromeService(executable_path=chromedriver_path)

# Read the credentials from the configuration file
config = configparser.ConfigParser()
config.read('/var/kiosk/conf/config.ini')

# URL of the webpage you want to open
url = config.get('Url', 'url')

username = config.get('Credentials', 'username')
password = config.get('Credentials', 'password')

# If the credentials are not found or empty, prompt the user to enter them interactively
if not username:
    username = input('Enter your username: ')

if not password:
    password = input('Enter your password: ')

# Launch Firefox browser using geckodriver
driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

# Open the webpage
driver.get(url)

# Find and click the "Sign In" button
sign_in_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="start-page-app"]/div[2]/div[1]/ul/li[3]/a')))
sign_in_button.click()

# Find the username and password fields and fill them with the credentials
username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userName"]')))
password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))

username_field.send_keys(username)
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the page to load after logging in (you can modify the wait time if needed)
wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-nav"]/ul/li[6]/a/img')))

# Click the "Check-In" button
check_in_button = driver.find_element(By.XPATH, '//*[@id="main-nav"]/ul/li[6]/a/img')
check_in_button.click()

# Find and click the "More Options" button
more_options_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-more')))
more_options_button.click()

# Find and click the "Launch Kiosk" button
launch_kiosk_button = driver.find_element(By.XPATH, '//*[@id="checkInProfiles_table"]/tbody/tr/td[6]/ul/li/ul/li[1]/a')
launch_kiosk_button.click()

# Find and click the radial dial for "Check-In & Sign-Up Mode"
check_in_sign_up_mode_dial = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="check-in-type-add"]')))
check_in_sign_up_mode_dial.click()

# Find and click the "Launch Kiosk" button again
launch_kiosk_button2 = driver.find_element(By.XPATH, '//*[@id="launch-kiosk-dialog"]/div[2]/a[1]')
launch_kiosk_button2.click()

# Determine what to do for shutdown and timing
sleep_time = int(config.get('Shutdown', 'sleep_time'))
shutdown_host = config.getboolean('Shutdown', 'shutdown_host')

# Add a delay to keep the Kiosk window open for a certain duration
time.sleep(sleep_time)

# Check the shutdown behavior configuration
if shutdown_host:
    # Execute the shutdown command
    os.system('shutdown /s /t 0')
else:
    # Exit the script
    sys.exit()
