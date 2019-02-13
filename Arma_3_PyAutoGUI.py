# How to Open Arma 3 in Python using pywinauto
# make sure that the path here is identical to your Arma executable on your PC

# necessary imports
import pyautogui
import subprocess
import time
from win32api import GetSystemMetrics

# get the width of the user's resolution
# this is used for the auto clicking coordinates
userWidth = GetSystemMetrics(0)
userHeight = GetSystemMetrics(1)

# open the game and sleep to wait for the game to open
print('Press Ctrl-C at any time in this window to stop.')
print('This is your resolution: ' + str(userWidth) + ' x ' + str(userHeight))
subprocess.Popen(['C:\\Program Files (x86)\\Steam\\steamapps\\common\\Arma 3\\Arma3_x64.exe'])
time.sleep(140)

if userWidth == 1366:

    # this click will open the editor mao select screen
    pyautogui.click(1020, 364, button='left')

    time.sleep(3)

    # this clicks on the map "Altis"
    pyautogui.click(375, 126, button='left')

    time.sleep(1)

    # this clicks on the confirm button to load Altis
    pyautogui.click(1021, 672, button='left')

    time.sleep(45)

    # this click opens the tools menu bar option
    pyautogui.click(359, 11, button='left')

    time.sleep(1)

    # this click opens the console
    pyautogui.click(411, 53, button='left')

elif userWidth == 1920:

    # this click will open the editor mao select screen
    pyautogui.click(1302, 598, button='left')

    time.sleep(3)

    # this clicks on the map "Altis"
    pyautogui.click(692, 288, button='left')

    time.sleep(1)

    # this clicks on the confirm button to load Altis
    pyautogui.click(1262, 808, button='left')

    time.sleep(45)

    # this click opens the tools menu bar option
    pyautogui.click(256, 6, button='left')

    time.sleep(1)

    # this click opens the console
    pyautogui.click(286, 34, button='left')

else:
    print('Your resolution is currently unsupported by this script. Please re-run the script using')
    print('one of the supported resolutions.')
    exit(1)