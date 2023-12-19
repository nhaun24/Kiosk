import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pyvirtualdisplay import Display
import configparser
import sys
import subprocess
import tempfile

#display = Display(size=(1920, 1080)).start()
# Set up Xvfb
#xvfb_command = "Xvfb :0 -screen 0 1920x1080x24"
#subprocess.Popen(xvfb_command, shell=True)

# Set the DISPLAY environment variable
#os.environ['DISPLAY'] = ':0'

# Set up virtual display
display = Display(visible=0, size=(1920, 1080))
display.start()

# Set the DISPLAY environment variable
os.environ['DISPLAY'] = display.new_display

# wait for host to initialise. can change this timer
print("Please wait for host to initialize, do not exit from this screen")
time.sleep(1)

# Change directory to the specified path
os.chdir(r"/var/kiosk")

# Execute the Git pull command
os.system('git pull --no-verify https://github.com/nhaun24/Kiosk Linux')

# Specify tempfile stuff
temp_user_data_dir = tempfile.mkdtemp()
temp_cache_dir = tempfile.mkdtemp()

# Path to the edgedriver executable
#driver_path = '/usr/bin/chromium-browser'
driver_path = ChromeDriverManager().install()

# Create Chrome service
chrome_service = ChromeService(executable_path=driver_path)

# Create Chrome options class
chrome_options = webdriver.ChromeOptions()

# Create Chrome options
chrome_options.add_argument(f'--user-data-dir={temp_user_data_dir}')
chrome_options.add_argument(f'--disk-cache-dir={temp_cache_dir}')
#chrome_options.binary_location = "/usr/bin/chromium-browser"
#chrome_options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36)
#chrome_options.add_argument('--disable-software-rasterizer')
#chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized') 
#chrome_options.add_argument('--disable-infobars')
#chrome_options.add_argument('--disable-popup-blocking')
#chrome_options.add_argument('--disable-extensions')
#chrome_options.add_argument('--disable-notifications')
#chrome_options.add_argument('--disable-save-password-bubble')
#chrome_options.add_argument('--enable-logging')
#chrome_options.add_argument('--disable-session-crashed-bubble')
#chrome_options.add_argument('--kiosk')
chrome_options.add_argument('--service_args=--wait-for-browser=600')

# Read the credentials from the configuration file
config = configparser.ConfigParser()
config.read(r'/var/kiosk/conf/config.ini')

# URL of the webpage you want to open
url = 'https://onrealm.org/fbcathens/Home/Tasks?redirectController=Individual&redirectAction=Info&redirectId=b1639cf8-8fc1-4287-a213-ad7a0148dd6a'

username = config.get('Credentials', 'username')
password = config.get('Credentials', 'password')

# If the credentials are not found or empty, prompt the user to enter them interactively
if not username:
    username = input('Enter your username: ')

if not password:
    password = input('Enter your password: ')


# Launch Web Driver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

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
#shutdown_host = config.getboolean('Shutdown', 'shutdown_host')
#shutdown_or_restart = config.get('Shutdown', 'shutdown_or_restart').lower()

# Add a delay to keep the Kiosk window open for a certain duration
time.sleep(sleep_time) 

os.system('sudo shutdown 13:00')
# Check the shutdown behavior configuration
#if shutdown_or_restart == 'shutdown':
    # Execute the shutdown command
#     os.system('sudo poweroff') 
#elif shutdown_or_restart == 'restart':
    # Execute the restart command
 #   os.system('sudo reboot') 
