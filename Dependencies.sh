#!/bin/bash

# Update package list
sudo apt update

# Install Geckodriver
sudo apt-get install firefox-geckodriver

# Install Python 3
sudo apt-get install python3

# Install QZ-tray
wget -qO - qz.sh | bash

# Install Python dependencies using pip
sudo apt-get install python3-pip

# Install required Python packages
pip3 install configparser sysconfig subprocess selenium

# Additional packages that are part of the standard library, so no need to install
# - os
# - time

echo "Dependencies installed successfully."
