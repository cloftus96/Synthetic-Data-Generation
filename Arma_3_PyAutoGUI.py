#*********************************************************************************
#
# HOW TO OPEN THE COMMAND WINDOW IN ARMA 3 USING PYAUTOGUI
#
# MAKE SURE THAT THE PATH IN THE subprocess COMMAND IS IDENTICAL
# TO THAT OF YOUR OWN ARMA 3 64 BIT EXECUTABLE
#
# This script opens the game Arma 3 and uses simulated clicks to navigate
# to the console and open it. It then types a command into the console
# which runs any Arma 3 script you would like
#
#*********************************************************************************
#
# This script uses three main functions of pyautogui:
#
#    moveTo - this function moves the cursor to the desired pixel on the screen.
#    The pixel is designated by using the coordinates within the resolution,
#    starting from the top left corner of the screen
#    Examples: (0,0) is the very top left pixel
#              (960, 540) would be in the middle of the screen on 1920x1080
#
#    click - a simple function that just automates a click at the current mouse
#    coordinate. Default is a right click, the paramater here is added to make it
#    a left click.
#
#    More documentation of pyautogui functions can be found at:
#           https://pyautogui.readthedocs.io/en/latest/
#
#**********************************************************************************

# necessary imports
import pyautogui
import subprocess
import time
from win32api import GetSystemMetrics


def main():
    print('------------------------------------')
    print('ARMA 3 SCRIPT EXECUTOR IN PYTHON 3.7')
    print('------------------------------------')

    # get the width and height of the user's resolution
    # this is used for the auto clicking coordinates
    userWidth = GetSystemMetrics(0)
    userHeight = GetSystemMetrics(1)

    print('')
    print('Press Ctrl-C at any time in this window/terminal to stop.')
    print('')
    print('This is your resolution: ' + str(userWidth) + ' x ' + str(userHeight))
    print('')

    # check the users resolution and go to his/her respective coordinates
    # 1366x768
    if userWidth == 1366:

        # open the game and sleep to wait for the game to open
        # before running, change this path to the Arma3_64.exe file on your own computer
        try:
            subprocess.Popen(['C:\\Program Files (x86)\\Steam\\steamapps\\common\\Arma 3\\Arma3_x64.exe'])
        except FileNotFoundError:
            print('ERROR:')
            print('The path to the Arma3_x64 executable is incorrect for this system. Please change the path in the '
                  'script or the path to the game to properly reflect the correct path in both places.')
            exit(1)
        else:
            time.sleep(130)

            # this click will open the editor map select screen
            pyautogui.moveTo(1020, 364, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(3)

            # this clicks on the map "Altis"
            pyautogui.moveTo(375, 126, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # this clicks on the confirm button to load Altis
            pyautogui.moveTo(1021, 672, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(60)

            # this click opens the scenario menu bar option
            pyautogui.moveTo(60, 10, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # this click hits open (to open the mission open window)
            pyautogui.moveTo(73, 82, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # this click physically opens the mission
            pyautogui.moveTo(963, 716, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # this click opens the play menu bar option
            pyautogui.moveTo(511, 12, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(3)

            # this click runs the mission in single player
            pyautogui.moveTo(612, 82, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # this click gets rid of an automatic error window
            pyautogui.moveTo(1139, 726, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # # run the script with a click
            # pyautogui.moveTo(890, 351, 1)
            # time.sleep(1)
            # pyautogui.click(button='left')
            #
            # time.sleep(1)
            #
            # # cancel out of the console once the script is run (not done automatically)
            # pyautogui.moveTo(501, 675, 1)
            # time.sleep(1)
            # pyautogui.click(button='left')

    # 1920x1080
    elif userWidth == 1920:

        # open the game and sleep to wait for the game to open
        # before running, change this path to the Arma3_64.exe file on your own computer
        try:
            subprocess.Popen(['C:\\Program Files (x86)\\Steam\\steamapps\\common\\Arma 3\\Arma3_x64.exe'])
        except FileNotFoundError:
            print('ERROR:')
            print('The path to the Arma3_x64 executable is incorrect for this system. Please change the path in the '
                  'script or the path to the game to properly reflect the correct path in both places.')
            exit(1)
        else:
            time.sleep(130)

            # this click will open the editor map select screen
            pyautogui.moveTo(1302, 598, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(3)

            # this clicks on the map "Altis"
            pyautogui.moveTo(692, 295, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # this clicks on the confirm button to load Altis
            pyautogui.moveTo(1262, 808, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(45)

            # this click opens the scenario menu bar option
            pyautogui.moveTo(36, 8, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # this click hits open (to open the mission open window)
            pyautogui.moveTo(78, 58, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # this click physically opens the mission
            pyautogui.moveTo(1158, 866, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # this click opens the play menu bar option
            pyautogui.moveTo(360, 6, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # this click runs the mission in single player
            pyautogui.moveTo(464, 60, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # this click gets rid of an automatic error window
            pyautogui.moveTo(1772, 1044, 1)
            time.sleep(1)
            pyautogui.click(button='left')

            time.sleep(1)

            # # this click opens the console
            # pyautogui.moveTo(286, 34, 1)
            # time.sleep(1)
            # pyautogui.click(button='left')

            # # type the command to run the txt
            # # this path is tentative. The full script will eventually create this file and place it in THIS path,
            # # so this path SHOULD NOT BE CHANGED.
            # pyautogui.typewrite(r'_handle = player execVM "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Arma 3\\Data_Generator.sqf"; ')
            # pyautogui.typewrite('waitUntil {scriptDone _handle};')
            #
            # # run the script with a click
            # pyautogui.moveTo(1130, 509, 1)
            # time.sleep(1)
            # pyautogui.click(button='left')
            #
            # time.sleep(1)
            #
            # # cancel out of the console once the script is run (not done automatically)
            # pyautogui.moveTo(786, 804, 1)
            # time.sleep(1)
            # pyautogui.click(button='left')

    # if you go into this else block, the user has a resolution that is not supported yet
    # by this script
    # i.e. the coordinates have not been found for each click for that specific resolution
    else:
        print('ERROR:')
        print('Your resolution is currently unsupported by this script. Please re-run the script using')
        print('one of the supported resolutions.')
        exit(2)


if __name__ == '__main__':
    main()
