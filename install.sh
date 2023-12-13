#!/bin/bash

# Update package list
sudo apt update

# Install WebDriver
sudo apt-get install chromium-chromedriver -y

# Install Python 3
sudo apt-get install python3 -y

# Install QZ-tray
wget -qO - qz.sh | bash

# Install xvfb
sudo apt-get install xvfb -y
# Install Python dependencies using pip
sudo apt-get install python3-pip -y

# Install required Python packages
sudo pip3 install configparser
sudo pip3 install selenium

sudo cd /var
sudo mkdir kiosk
sudo cd kiosk
sudo git init
sudo git pull --no-verify https://github.com/nhaun24/Kiosk Linux
sudo mkdir conf
sudo cp config.ini /var/kiosk/conf


echo "Installed successfully. Remember to change the config.ini file"

