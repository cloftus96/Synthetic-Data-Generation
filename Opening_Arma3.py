# How to Open Arma 3 in Python
# make sure that the path here is identical to your Arma execuatble on your PC

# necessary imports
from pynput.keyboard import Key, Controller
import subprocess
import time

# create the simulated keyboard
keyboard = Controller()

# Open Arma 3
subprocess.Popen(['C:\Program Files (x86)\Steam\steamapps\common\Arma 3\Arma3.exe'])

# wait for the cpu to open the game
time.sleep(180)

# simulate keystrokes to open the editor
# right arrow 3 times then enter
# give 10 seconds between each keystroke

# right arrow
keyboard.press(Key.right)
keyboard.release(Key.right)

time.sleep(2)

keyboard.press(Key.right)
keyboard.release(Key.right)

time.sleep(2)

keyboard.press(Key.right)
keyboard.release(Key.right)

time.sleep(2)

# enter
keyboard.press(Key.enter)
keyboard.release(Key.enter)

# wait 30 seconds for editor to open map selection
time.sleep(30)

# simulate keystrokes to choose Altis (the map)
# three up arrows then enter

# up arrow
keyboard.press(Key.up)
keyboard.release(Key.up)

time.sleep(2)

keyboard.press(Key.up)
keyboard.release(Key.up)

time.sleep(2)

keyboard.press(Key.up)
keyboard.release(Key.up)

time.sleep(2)

# enter
keyboard.press(Key.enter)
keyboard.release(Key.enter)

# give 3 more minutes for the map to open
time.sleep(180)

# open the console in game
keyboard.press('`')

# write the scripts here!
