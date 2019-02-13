# How to Open Arma 3 in Python using pywinauto
# make sure that the path here is identical to your Arma executable on your PC

# necessary imports
import pyautogui
import subprocess
import time

print('Press Ctrl-C at any time in this window to stop.')

subprocess.Popen(['C:\Program Files (x86)\Steam\steamapps\common\Arma 3\Arma3_x64.exe'])

time.sleep(150)

# editor
pyautogui.click(1020, 364, button='left')

time.sleep(15)

# altis
pyautogui.click(375, 126, button='left')

time.sleep(1)

# confirm altis
pyautogui.click(1021, 672, button='left')

time.sleep(45)

# tools
pyautogui.click(359, 14, button='left')

time.sleep(1)

# console
pyautogui.click(411, 53, button='left')