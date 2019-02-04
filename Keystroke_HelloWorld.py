# Basic script using simulated keystrokes
# this should write Hello World in your current window,
# (except the console since it is running the script)
# and then press the windows key

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(2)
for char in "Hello World":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(1)
else:
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
