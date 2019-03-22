# Using Arma 3 to Generate Synthetic Data

This README details how python and Arma 3 script(s) are used to
generate data for a Neural Network using the editor from the
game Arma 3. It also gives system requirements and many 
other changes that must be made by the user in order for the
python script to run.

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
to the editor on the map "Altis," an Arma 3 "mission" is then
run. This mission will be the Arma 3 script that was created at the
start of the python script. This Arma 3 script will generate the object that the neural
network needs pictures of, and start taking screenshots of it.
Then, the Python script will run in the background, and
manage the screenshots created by putting them in 
appropriate folders. Once all of the pictures have been taken,
Python then closes the game and exits.

### Notes
In order for the script to work correctly:
- The game Arma 3 **AND** Steam must **BOTH** be installed **and** updated. 
This script opens the game directly from the executable instead 
of the launcher, and if the game or Steam is not updated, 
not only will the sleep times be off due to updates, but the
executable file will just load the launcher, which will not
work.
- The script has multiple instances of the Arma 3 executable 
(arma3_x64.exe) path. This file is typically installed to this
folder:
 
    C:\Program Files (x86)\Steam\steamapps\common\Arma 3

  This is the path used in the script. However, this can 
  change from system to system. Make sure that each instance of 
  this path corresponds to the correct path in your system.
 
- Some times of day are so dark that nothing can be seen
(the times we believe are roughly from 12am-5am). There is
a night vision mode in the game, but it is not implemented
for this project.
- Current supported resolutions are 1920x1080, and 1366x768.
More resolutions may be added in the future.
- This project uses Python scripts. The python 3.7 interpreter
must be installed on the system in order for the the main
script in this project to run.

### Error Codes
- Error Code 0: Script ran as intended
- Error Code 1: Path to the game executable is incorrect
- Error Code 2: Resolution unsupported by script
- Error Code 3: Issue with .sqf file creation

## Necessary Installations
Use these commands in the Windows terminal to install required
packages:

```windows
pip install pyautogui
pip install pypiwin32
```

If you have the python terminal open instead, use these commands:

```
install pyautogui
install pypiwin32
```

