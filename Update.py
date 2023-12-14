import os
import sys

# Change directory to the specified path
os.chdir(r"/var/kiosk")

# Execute the Git pull command
os.system('git pull --no-verify https://github.com/nhaun24/Kiosk main')
