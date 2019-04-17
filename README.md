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
manage the screenshots created by putting them in an
appropriate folder. Once all of the pictures have been taken,
Python then closes the game and exits.

### Notes
In order for the script to work correctly:
- Python 3.7 must be installed, preferably to the path %HOMEDIRECTORY%\Python37.
    - This is the version that the script was tested on. The
    script is not guaranteed to work on any other version.
- This script also uses MATLAB 2018b. It is **imperative** that
this specific version is installed, as the script uses a function
that only this version has.
- The game Arma 3 **AND** Steam must **BOTH** be installed **and** updated. 
This script opens the game directly from the executable instead 
of the launcher, and if the game or Steam is not updated, 
not only will the sleep times be off due to updates, but the
executable file will just load the launcher, which will not
work.
- Before running this project, run the game Arma 3 once
beforehand, and ensure two things:
    - all necessary licenses have been accepted.
    - resolution is changed to whatever is native, and the
    game changed to fullscreen
- Make sure that the game Arma 3 is **closed** before running
this project. Having two copies of the game open may cause
unnecessary lag.
- The script has multiple instances of the Arma 3 executable 
(arma3_x64.exe) path. This file is typically installed to this
folder:
 
    %HOMEDIRECTORY%\Program Files (x86)\Steam\steamapps\common\Arma 3

  This is the path used in the script. However, this can 
  change from system to system. Make sure that each instance of 
  this path corresponds to the correct path in your system.
 
- Some times of day are so dark that nothing can be seen
(the times we believe are roughly from 12am-5am). There is
a night vision mode in the game, but it is not implemented
for this project.
- Current supported resolutions are 1920x1080, and 1366x768.
More resolutions may be added in the future.
- The script moves the screenshots to this folder:

    %HOMEDIRECTORY%\Users\\%MainUser%\Documents\SyntheticDataGen

  Ensure before running the project that this directory is either
  empty or non-existant.

### Error Codes
- Error Code 0: Script ran as intended
- Error Code 1: Path to the game executable is incorrect
- Error Code 2: Resolution unsupported by script
- Error Code 3: Issue with .sqf file creation
- Error Code 4: Issue with the file merging process

## Necessary Installations
Use these commands in the Windows terminal to install required
packages:

```windows
python -m pip install pyautogui
python -m pip install pypiwin32
```

It is recommended to run this command before you install 
these two packages:

```windows
python -m pip install --upgrade pip
```

*Note: depending on where your python is installed or what
exact version you have, you may need to use the command "py"
instead of "python."*

If you have the python terminal open instead, use these commands:

```
install pyautogui
install pypiwin32
```

## Custom Vehicles
Follow these steps if you would like to use custom vehicles
with this script instead of default vehicles:

1. Open Steam and click on Library
2. Click Tools in the drop down menu
3. Scroll to the top (if necessary) and install "Arma 3 Tools"
and "Arma 3 Samples" by double clicking on them.
4. Run "Arma 3 Tools" by double clicking on it. Choose the option
"Play Arma 3 Tools."
5. When the Arma 3 Tools Window Opens click on "Project
Drive Management."
6. In the window that opens, first click "Install Buldozer"
then "Run," and accept any windows that pop up.
7. Once this is finished, click "Extract Game Data" then run,
and accept any windows that pop up.
    1. Note - these windows may mention something about purging
    data. All of the data this script creates can be recreated,
    so do not worry about this. However, if you have any missions
    or any other data that you want to save, look into backing
    it up before doing this.
8. While the game data is extracting, click on "Mount the work drive (P)"
and then run, accepting any appearing text boxes. Both of these
may take awhile.
9. 


## Examples
Here are some examples of the data that this script creates:

![Example 1 from Factory.](https://github.com/cloftus96/Synthetic-Data-Generation/blob/Image-Processing/Example_1_Factory.png "Example 1 from Factory")

![Example 2 from Desert.](https://github.com/cloftus96/Synthetic-Data-Generation/blob/Image-Processing/Example_2_Desert.png "Example 2 from Desert")

Here is one example of the image processing the script does
to generate the location of the vehicle. It first takes a
regular image, and then makes a copy of it without the vehicle.
It then compares the two to find the spot where the vehicle is:

![Picture with vehicle.](https://github.com/cloftus96/Synthetic-Data-Generation/blob/Image-Processing/im3.jpg "Picture with Vehicle")

![Picture without vehicle.](https://github.com/cloftus96/Synthetic-Data-Generation/blob/Image-Processing/im2.jpg "Picture without Vehicle")

![Picture Comparison.](https://github.com/cloftus96/Synthetic-Data-Generation/blob/Arma3_Script_Writing/Car_Point_Cloud.jpg "Picture Comparison")

