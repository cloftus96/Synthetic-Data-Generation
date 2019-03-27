import multiprocessing as mp
import os.path
from pathlib import Path
import sys
import ast
import time
import shutil
# import our functions
import Arma_3_PyAutoGUI
import main_script_generator
import image_manager


def main(map_pos, vehicle_names, cam_rota_angle_step, vehicle_rota_angle_step, cam_delay, cam_x_offset, fog_incr, time_incr):
    # generate script
    position_array = main_script_generator.position_generator(cam_rota_angle_step, cam_x_offset)
    main_script_generator.generate_script(map_pos, vehicle_names, position_array, vehicle_rota_angle_step)

    # create a process whose job is to run the file mover code
    image_file_manager = mp.Process(target=image_manager.image_file_mover, args=(cam_delay/2,))
    image_file_manager.start()

    # once we have the script, run the game and execute the script within it
    Arma_3_PyAutoGUI.main()


if __name__ == '__main__':
    """ Expected Positional Arguments:
        1) map_pos : 
        2) vehicle_names :
        3) cam_rota_angle_step : (degrees)
        4) vehicle_rota_angle_step : degrees
        5) cam_delay : The time it takes for the camera to move the to next screenshot position
        6) cam_x_offset : The initial x coordinate offset of the camera from the vehicle in Arma 3
        7) fog_incr :  The increment in fog value in Arma 3. Range of fog values are 0.0 - 0.8 , so User should select
            a value lower than 0.8 if they wish for fog to show up in the dataset. However, to disable fog, >0.8 can be used.
        8) time_incr :  The increment in time of day in Arma 3. This is in 24-hour time, and accepts fractional hours.
            e.g. 1.5 would result in time of day increments of one hour and thirty minutes.
    """
    # Use Abstract Syntax Tree to evaluate tuples and lists in cmd line args
    map_pos = ast.literal_eval(sys.argv[1])
    vehicle_names = ast.literal_eval(sys.argv[2])
    cam_rota_angle_step = float(sys.argv[3])
    vehicle_rota_angle_step = float(sys.argv[4])
    cam_delay = float(sys.argv[5])
    cam_x_offset = float(sys.argv[6])
    fog_incr = float(sys.argv[7])
    time_incr = float(sys.argv[8])
    main(map_pos, vehicle_names, cam_rota_angle_step, vehicle_rota_angle_step, cam_delay, cam_x_offset, fog_incr, time_incr)

