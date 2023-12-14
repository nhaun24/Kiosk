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
pip3 install configparser selenium


echo "Dependencies installed successfully."
