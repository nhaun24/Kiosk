# Kiosk
.py code for remote kisok update opperations

PREREQS*******************************************

MSEdgedriver (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

GIT(https://git-scm.com/downloads)

Python3.10 (https://www.python.org/downloads/windows/)

**************************************************




PYTHON PACKAGE DEPENDENCIES***********************

	pip install selenium

	pip install configparser

	pip install msedge-selenium-tools

**************************************************




SETUP*********************************************

Open GIT GUI
	clone https://github.com/nhaun24/Kiosk
		to /documents

Install Python3.10
	Must add to path
	Must disable path length limit

Open Python3.10
	Install Python Package Dependencies(see above)

Edit config.ini
Place config.ini in c:/Program Files



The config.ini file is used to store configuration options for the script. It allows you to customize the behavior of the script by specifying values for various parameters.

Place the config.ini file in the Program Files directory. Be sure to modify the provided .ini file to reflect your variables

The sleep_time option determines the duration, in seconds, to wait before initiating the shutdown process. Set this value according to your requirements.

The shutdown_host option controls the behavior of the shutdown process. Set it to either yes or no to determine whether the script should shut down the host or only close the application. For example: