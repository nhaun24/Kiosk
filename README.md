# Kiosk
.py code for use with onrealm PC based Kiosks, to automate the startup procedure.
	This code uses a mix of Python librarys and Git to make your onrealm public facing kiosks 100% remote and in no need of interaction.
 	The code starts by checking for updates on the main branch of this repository, then downloads them. It then goes on to open QZ-Trey, which is vital for printing from the kisok software.
   	After that, it looks through the config.ini file to locate the URL and credentials for your onrealm instance. From there it goes about navigating the website to land you on the kiosk page.
    	Finally it waits for however long you have it set for in the config.ini file, then either closes all apps, or shutsdown the host depending on your preferences. 
     This code is commented pretty hevily, and what is not explained in the code, will most likely be in this read me.

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

The sleep_time option determines the duration, in seconds, to wait before initiating the shutdown process. VALUE IS MEASURED IN SECONDS, please change accordingly.

The shutdown_host option controls the behavior of the shutdown process. Set it to either yes or no to determine whether the script should shut down the host or only close the application. Var must be [yes] to shut down, any other char will result in program not shutting down host.
