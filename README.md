# Using Arma 3 to Generate Synthetic Data

This README details the ins and outs of the script(s) used to
generate data for a Neural Network using the editor from the
game Arma 3. It also gives system requirements and many 
other changes that must be made by the user in order for the
script to run.

## Description
The intention of this script is to create images to further 
develop a neural network. The script generates roughly 
20,000+ images in different environment settings and locations,
from multiple different angles. Some examples of different 
environments are fog, sun, rain, etc.

The Python script starts by writing the Arma 3 script. This
script will get stored in a separate file for later use. It
then opens the game on the system and navigates through the
menu to the editor using an autoclick function. After getting
to the editor on the map "Altis," the console is then opened.
After the console is opened, a command is typed into the 
console using simulated keystrokes. This command will read in
the previously created .sqf file, which is the file type of
an Arma 3 script. The command runs the script after reading 
it. This script will generate the object that the neural
network needs pictures of, and start taking screenshots of it.
Then, the Python script will run in the background, and
manage the screenshots created by putting them in 
appropriate folders. Once all of the pictures have been taken,
Python then closes the game and exits.

### Notes
In order for the script to work correctly:
- The game Arma 3 AND Steam must BOTH be installed and updated. 
This script opens the game directly from the executable instead 
of the launcher, and if the game or Steam is not updated, 
not only will the sleep times be off due to updates, but the
executable file will just load the launcher, which will not
work.
- The script has multiple instances of the Arma 3 executable 
(arma3_x64.exe) path. This file is typically installed to the
folder C:\Program Files (x86)\Steam\steamapps\common\Arma 3,
which is the path used in the script. However, this can 
change from system to system. Make sure that each instance of 
this path corresponds to the correct path in your system. 
- The console in Arma 3 must be completely cleared. Closing
the game itself will not clear the commands in the command 
window, so they must be manually cleared so that when the 
script adds the code, it is not compromised.
- Some times of day are so dark that nothing can be seen
(the times we believe are roughly from 12am-5am). There is
a night vision mode in the game, but it is not implemented
for this project.
- Current supported resolutions are 1920x1080, and 1366x768.
More resolutions may be added in the future.

### Error Codes
- Error Code 0: Script ran as intended
- Error Code 1: Path to the game executable is incorrect
- Error Code 2: Resolution unsupported by script
- Error Code 3: Issue with .sqf file creation

## Necessary Installations
Use these commands in the Python terminal to install required
packages:

```windows
pip install pyautogui
pip install pypiwin32
```

