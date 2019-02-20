# Using Arma 3 to Generate Synthetic Data

This README details the ins and outs of the script(s) used to generate data for a Neural Network using the editor from the game Arma 3. It also gives system requirements and many other changes that must be made by the user in order for the script to run.

## Description
The intention of this script is to create images to further develop a nerual network. 
The script generates roughly 20,000+ images in different environment settings and locations, from multiple different angles. Some examples of different environments are fog, sun, rain, etc.

### Notes
In order for the script to work correctly:
- The game Arma 3 AND Steam must BOTH be updated. This script opens the game directly from the executable instead of the launcher, and if the game or steam is not updated, not only will the sleep times be off due to updates, but the executable file will just load the launcher, which will not work.
- The script has multiple instances of the Arma 3 executable path (arma3_x64.exe). This file is typically installed to the folder C:\Program Files (x86)\Steam\steamapps\common\Arma 3\\, which is the path used in the script. However, this can change system to system. Make sure that each instance of this path in this script corresponds to the correct path of your system. 
- The console in Arma 3 must be completely cleared. Closing the game itself will not clear the commands in the command window, so they must be manually cleared so that when the script adds the code, it is not compromised.

### Error Codes
- Error Code 0: Script ran as intended
- Error Code 1: Path to the game executable is incorrect
- Error Code 2: Resolution unsupported by script

## Necessary Installations
Use these commands in the Python terminal to install required packages:

```windows
pip install pyautogui
pip install pypiwin32
```

