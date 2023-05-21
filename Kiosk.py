import time
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import configparser
import sys

def update_and_restart():
    # Change directory to the specified path
    os.chdir(r"C:\Users\Admin\Documents\Get")

    # Execute the Git pull command
    subprocess.call(['git', 'pull', 'https://github.com/nhaun24/Kiosk', 'main'])

    # Restart the script with the updated version
    python = sys.executable
    os.execl(python, python, *sys.argv)

def main():
    # Check for updates and restart if necessary
    update_and_restart()

    # Path to the edgedriver executable
    driver_path = '/path/to/edgedriver'

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

    # Rest of your script...
    # Open the webpage
    driver.get(url)

    # Find and click the "Sign In" button
    sign_in_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="start-page-app"]/div[2]/div[1]/ul/li[3]/a')))
    sign_in_button.click()

    # Rest of your script...

    # Check the shutdown behavior configuration
    shutdown_host = config.getboolean('Shutdown', 'shutdown_host')

    # Add a delay to keep the Kiosk window open for a certain duration
    time.sleep(sleep_time) 

    if shutdown_host:
        # Execute the shutdown command
        os.system(f'shutdown /s /t 0')
    else:
        # Exit the script
        sys.exit()

if __name__ == "__main__":
    main()
