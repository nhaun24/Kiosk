import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import configparser
import sys
import subprocess

# Path to the QZ Tray application executable
qz_tray_path = r"C:\Program Files\QZ Tray\qz-tray.exe"

# Launch the QZ Tray application
subprocess.Popen(qz_tray_path)

# Change directory to the specified path
os.chdir(r"C:\Program Files\repo")

# Execute the Git pull command
os.system('git pull --no-verify https://github.com/nhaun24/Kiosk main')

# Path to the edgedriver executable
driver_path = 'C:\Program Files'

# Create Edge options
edge_options = Options()
edge_options.use_chromium = True
edge_options.add_argument("--kiosk")  # Add this argument to start the browser in full-screen mode

# URL of the webpage you want to open
url = 'https://onrealm.org/fbcathens/Home/Tasks?redirectController=Individual&redirectAction=Info&redirectId=b1639cf8-8fc1-4287-a213-ad7a0148dd6a'

# Read the credentials from the configuration file
config = configparser.ConfigParser()
config.read(r'C:\Program Files\config.ini')

username = config.get('Credentials', 'username')
password = config.get('Credentials', 'password')

# If the credentials are not found or empty, prompt the user to enter them interactively
if not username:
    username = input('Enter your username: ')

if not password:
    password = input('Enter your password: ')


# Launch Microsoft Edge browser using edgedriver
driver = webdriver.Edge(executable_path=driver_path, options=edge_options)

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

# Determine what to do for shutdown and timeing
sleep_time = int(config.get('Shutdown', 'sleep_time'))
shutdown_host = config.getboolean('Shutdown', 'shutdown_host')

# Add a delay to keep the Kiosk window open for a certain duration
time.sleep(sleep_time) 

# Check the shutdown behavior configuration
if shutdown_host:
    # Execute the shutdown command
    os.system(f'shutdown /s /t 0')
else:
       # Exit the script
    sys.exit()
