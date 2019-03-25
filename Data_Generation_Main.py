import multiprocessing as mp
import os.path
from pathlib import Path
import sys
import time
import shutil
# import our functions
import Arma_3_PyAutoGUI
import main_script_generator
import multiprocess_manager


def main(map_pos, vehicle_name, cRotaAngleStep, xDist, platformRotaStep, cc):
    # generate script
    position_array = main_script_generator.position_generator(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    main_script_generator.generate_script(position_array, int(sys.argv[3]))
    # create a process whose job is to run the file mover code
    image_file_manager = mp.Process(target=image_file_mover, args=(cc/2,))
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

