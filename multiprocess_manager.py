import multiprocessing as mp
import os.path
from pathlib import Path
import sys
import time
import shutil
# import our functions
import Arma_3_PyAutoGUI
import main_script_generator


def image_file_mover(output_dir, check_delay):
    """ This function will check a pre-determined directory for pre-determined file name and will continue to check,
    sleeping for <check_delay> seconds between each check. If the file exists, it will move it to a separate
    pre-determined directory. check_delay should be 1/2 the time it takes to rotate the camera to the next position.
    """
    img_ctr = 1
    done = False
    # check for file in ~/arma3/
    screenshot_path = Path(os.path.expanduser('~\\Documents\\Arma 3\\Screenshots'))
    # if not screenshot_path.exists(): # I will fix this later
        # need to do some error stuff here
    while not done:
        # screenshot = Path(screenshot_path, '\\', file_name)
        screenshot = Path(screenshot_path, '\\arma3screenshot')  # for now this is hard-coded
        if screenshot.exists() and not screenshot.is_dir(): # how do i check for image files?
            # shutil.move(screenshot, Path(os.path.expanduser(output_dir, '\\', str(img_ctr), '.png')))
            shutil.move(screenshot, Path(os.path.expanduser('~\\Documents\\SyntheticDataGen\\', str(img_ctr), '.png')))
        img_ctr += 1  # increment the image counter after a successful move
        time.sleep(check_delay)  # sleep for check_delay seconds so we don't hammer the cpu unnecessarily


def main(cRotaAngleStep, xDist, platformRotaStep, outputDir, cc):
    # generate script
    position_array = main_script_generator.position_generator(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    main_script_generator.generate_script(position_array, int(sys.argv[3]))
    # create a process whose job is to run the file mover code
    image_file_manager = mp.Process(target=image_file_mover, args=(outputDir, cc/2,))
    image_file_manager.start()

    # once we have the script, run the game and execute the script within it
    Arma_3_PyAutoGUI.main()


if __name__ == '__main__':
    """ Expected Positional Arguments:
        1) Camera Rotation Angle Step Size (degrees)
        2) X-distance from Object to Place Camera
        3) Platform Rotation Angle Step (degrees)
        4) Directory into which to move the image files
        5) CC - the camera delay between shots
    """
    # create a process whose job is to run the file mover code
    #image_file_manager = mp.Process(target=image_file_mover, args=(sys.argv[4], sys.argv[5],))

