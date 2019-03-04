from pynput.keyboard import Key, Controller
import subprocess
import time

keyboard = Controller()

subprocess.Popen(['C:\Program Files (x86)\Steam\steamapps\common\The Jackbox Party Pack 5\The Jackbox Party Pack 5.exe'])

time.sleep(30)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(5)

keyboard.press(Key.down)
keyboard.release(Key.down)
time.sleep(1)
keyboard.press(Key.down)
keyboard.release(Key.down)
time.sleep(1)
keyboard.press(Key.up)
keyboard.release(Key.up)
time.sleep(1)
keyboard.press(Key.up)
keyboard.release(Key.up)
time.sleep(1)
keyboard.press(Key.esc)
keyboard.release(Key.esc)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)