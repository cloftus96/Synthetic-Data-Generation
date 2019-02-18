#*********************************************************************************
#
# HOW TO OPEN THE COMMAND WINDOW IN ARMA 3 USING PYAUTOGUI
#
# MAKE SURE THAT THE PATH IN THE subprocess COMMAND IS IDENTICAL
# TO THAT OF YOUR OWN ARMA 3 64 BIT EXECUTABLE
#
# This script opens the game Arma 3 and uses simulated clicks to navigate
# to the console and open it. It then types a command into the console
# which runs any Arma 3 script you would like
#
#*********************************************************************************

# necessary imports
import pyautogui
import subprocess
import time
from win32api import GetSystemMetrics

# get the width and height of the user's resolution
# this is used for the auto clicking coordinates
userWidth = GetSystemMetrics(0)
userHeight = GetSystemMetrics(1)

print('Press Ctrl-C at any time in this window to stop.')
print('This is your resolution: ' + str(userWidth) + ' x ' + str(userHeight))

# open the game and sleep to wait for the game to open
# before running, change this path to the Arma3_64.exe file on your own computer
subprocess.Popen(['C:\\Program Files (x86)\\Steam\\steamapps\\common\\Arma 3\\Arma3_x64.exe'])
time.sleep(130)

# check the users resolution and go to his/her respective coordinates
# 1366x768
if userWidth == 1366:

    # this click will open the editor map select screen
    pyautogui.click(1020, 364, button='left')

    time.sleep(3)

    # this clicks on the map "Altis"
    pyautogui.click(375, 126, button='left')

    time.sleep(1)

    # this clicks on the confirm button to load Altis
    pyautogui.click(1021, 672, button='left')

    time.sleep(60)

    # this click opens the tools menu bar option
    pyautogui.moveTo(363, 13, 1)
    time.sleep(1)
    pyautogui.click(button='left')

    time.sleep(3)

    # this click opens the console
    pyautogui.moveTo(411, 53, 1)
    time.sleep(1)
    pyautogui.click(button='left')

# 1920x1080
elif userWidth == 1920:

    # this click will open the editor map select screen
    pyautogui.click(1302, 598, button='left')

    time.sleep(3)

    # this clicks on the map "Altis"
    pyautogui.click(692, 295, button='left')

    time.sleep(1)

    # this clicks on the confirm button to load Altis
    pyautogui.click(1262, 808, button='left')

    time.sleep(45)

    # this click opens the tools menu bar option
    pyautogui.moveTo(256, 6, 1)
    time.sleep(1)
    pyautogui.click(button='left')

    time.sleep(1)

    # this click opens the console
    pyautogui.moveTo(286, 34, 1)
    time.sleep(1)
    pyautogui.click(button='left')

# if you go into this else block, the user has a resolution that is not supported yet
# by this script
# i.e. the coordinates have not been found for each click for that specific resolution
else:
    print('Your resolution is currently unsupported by this script. Please re-run the script using')
    print('one of the supported resolutions.')
    exit(1)