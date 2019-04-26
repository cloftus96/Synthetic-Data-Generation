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
to the editor, an Arma 3 "mission" is then
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
this **specific version** is installed, as the script uses a function
that only this version has.
- The game Arma 3 **AND** Steam must **BOTH** be installed **and** updated. 
If the game or Steam is not updated, the sleep times will be
off due to updates.
- Before running this project, run the game Arma 3 once
beforehand, and ensure two things:
    - all necessary licenses have been accepted.
    - resolution is changed to whatever is native, and the
    game changed to fullscreen
- Make sure that the game Arma 3 is **closed** before running
this project. Having two copies of the game open may cause
unnecessary lag.
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
and then run, accepting any appearing text boxes.
    1. Do this while Extract Game Data runs in the background,
    as Extract Game Data may take 30 mins to an hour or even 
    longer to complete.
    2. This function here creates a P: drive on your PC, and this
    is where Arma will take data from, and this is where custom
    data will be placed.
9. In the newly created P: drive, make a directory called 
"\Custom_Mods\Custom_Cars", or whatever you would like to
call it. Just make sure there is a directory to place your
custom file in.
    1. Some sample sites with custom files are listed here:
    
10. Take the .obj file that you would like to use and place
it in this directory, creating sub-directories for each as
you see fit.
11. Go back to the Arma 3 Tools application (see steps 1-4)
and click on "Object Builder."
12. Once in Object Builder, go to File->Import->OBJ File.
Locate your file in the directory that you chose and import
it.
13. Once imported, Object Builder will next ask you to scale
the object file. The number you put in here will depend on the
size of the object in the file. Start with 1, and play around
with different numbers until you get a sensible result. The
resulting object in the application should be no larger than
5x5x5 units on the graph the app provides.
14. Go to File->Options and ensure that next to External
Viewer, this path and command is listed:
    P:\buldozer.exe -buldozer -name=Buldozer -window -noLand
    -exThreads=0 -noLogs -noAsserts -cfg=p:\buldozer.cfg.
Hit ok once this is confirmed.
15. Now this is where some knowledge of 3D modeling is
helpful. There should be a red square in the toolbar; this
is Buldozer. When clicked, it should show a Start/Restart
option. Click this, and the 3d Modeler Buldozer will run.
This will show you what the model will look like in Arma.
    1. The controls in Buldozer are similar to that of most
    3D modelers. This guide will assume that you have your
    model just as you would like it in Arma. Buldozer is
    only here to ensure that what you have is correct.
    2. If the object does not look like what you want, you
    can edit it within the Object Builder application. The
    UI is not too hard to navigate, but a tutorial can be
    found here (set of 5 videos): #1 - https://youtu.be/VqSIcbUMdNo #2 - 
    https://youtu.be/v5f3QKGw46Q #3 - https://youtu.be/Fzzx8-KdhTs #4 - 
    https://youtu.be/v_yktoJhwBc #5 - https://youtu.be/ciXdmH2lCeo
    3. A lot of the details in these videos is unnecessary,
    it is merely included for documentation.
16. Now, in Object Builder, save the object as a .p3d file,
and put it in the same directory where you placed the .obj
file.
17. Next, a config file needs to be created so Arma can read
it as a car. Details about creating a config file can be found
in this video: https://youtu.be/jJ7E-Eov5mo. This file has
quite a lot in it, but for this purpose, a lot of it is
unnecessary. However, the video details every part of the
file, and what is needed to make it run.
18. Once the config file is created, go back to Steam->Library->
Tools->Arma 3 Tools. From here click "Launch Addon Builder."
19. In the source directory, choose the car directory you created
in step 9. In the destination directory, create a seperate
folder to place the packed data. Name this however you wish.
20. Once the data is packed, everything should be set! Go into
the Arma editor and choose any map you prefer. On the right hand
side of the window, search the name of your vehicle. If it is
not there, something may have gone wrong with the textures or config
of the vehicle. If it is there, click and drag it onto the world.
As long as everything went as it should have, the vehicle should
appear!

Troubleshooting for this process can be found in this Youtube
playlist: https://www.youtube.com/playlist?list=PL64QY_ftN4sHB86nnFJ866tmZj6BQFv_1

This is a very complicated process, so it may take time to create
and verify all of the necessary data.


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

