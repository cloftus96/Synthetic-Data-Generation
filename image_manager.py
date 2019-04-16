import os.path
from pathlib import Path
import time
import shutil
import csv
import math


def annotate()

def move_file(src, dest):
    """ Given a file 'src', move that file to the correct file specified by 'dest' """
    # exit with error code 4 if this fails...
    img_moved = False
    while not img_moved:
        try:
            shutil.move(src, dest)
        except OSError as e:
            if e.errno == 13:
                # print('File move error caught with OSError.errno 13') #  for debugging
                # This sleep could be 0.2 secs but I don't want to use this high a sleep time.
                # Could be an issue if the user makes the camera rotation time too low
                time.sleep(0.1)
                continue
            # raise the exception if it is not this particular error
            print('ERROR:')
            print('The image file mover process has encountered some unknown error. Please restart the script.')
            print('See the python error description here:')
            print(e)
            exit(4)
        # explicitly raise any other exception type
        except Exception as weirdE:
            print('ERROR:')
            print('The image file mover process has encountered some unknown error. Please restart the script.')
            print('See the python error description here:')
            print(weirdE)
            exit(4)
        img_moved = True

def image_file_mover(check_delay, config_params, cam_pos_list):
    """ This function will check a pre-determined directory for pre-determined file name and will continue to check,
    sleeping for <check_delay> seconds between each check. If the file exists, it will move it to a separate
    pre-determined directory. check_delay should be 1/2 the time it takes to rotate the camera to the next position.
    """
    img_ctr = 1
    blank_ctr = 1
    done = False
    num_cam_positions = 1 + math.floor(360/config_params['cam_rota_angle_step'])
    num_vehicle_rotations = 1 + math.floor(360/config_params['vehicle_rota_angle_step'])
    num_fog_settings = 1 + math.floor(0.8/config_params['fog_incr'])
    num_time_settings = 1 + math.floor(13.5/config_params['time_incr'])  # from 6 to 19.5
    num_vehicles = len(config_params['vehicle_names'])
    num_map_positions = len(config_params['map_positions'])
    num_images = num_map_positions * num_vehicles * num_cam_positions * num_vehicle_rotations * num_fog_settings * num_time_settings
    images_per_vehicle = num_images/num_vehicles
    images_per_vehicle_at_pos = images_per_vehicle/num_map_positions
    # vehicle is the top level loop construct

    # python lists
    map_pos_idx = 0
    vehicle_idx = 0
    fog_idx = 1


    screenshot_path = Path(os.path.expanduser('~\\Documents\\Arma 3\\Screenshots'))
    dest_dir = Path(os.path.expanduser('~\\Documents\\SyntheticDataGen'))
    if not Path.exists(dest_dir):
        os.makedirs(str(dest_dir), 0o777)  # create the directory if it doesnt exist
    # if not screenshot_path.exists(): # I will fix this later
        # need to do some error stuff here
    # open annotation csv file and write the header data. THIS WILL BLOW AWAY THE FILE CONTENTS
    annotation_file_path = Path(str(screenshot_path) + '\\AnnotationData.csv')
    annotation_csv = open(annotation_file_path, 'w+')
    annotation_writer = csv.writer(annotation_csv)
    annotation_writer.writerow(['filename','vehiclename','target_x','target_y','target_z','camera_x','camera_y','camera_z',
                               'foglevel','time','TR','BR','TL','BL'])
    annotation_csv.close()
    # re-open file for append to write the data. I will leave this file open for time concerns while moving files
    annotation_csv = open(annotation_file_path, 'a')
    while img_ctr <= num_images and blank_ctr <= num_images:
        screenshot = Path(str(screenshot_path) + '\\arma3screenshot.png')
        blank_screenshot = Path(str(screenshot_path) + '\\arma3blank.png')
        if screenshot.exists() and not screenshot.is_dir():
            # exit with error code 4 if this fails...
            dest = Path(os.path.expanduser('~\\Documents\\SyntheticDataGen\\' + str(img_ctr) + '.png'))
            move_file(screenshot, dest)

            # append this file's metadata to the annotation csv file here
            filename = '%s.png' % img_ctr
            data = [filename,
                    config_params['vehicle_names'][vehicle_idx],
                    config_params['map_positions'][map_pos_idx][0],
                    config_params['map_positions'][map_pos_idx][1],
                    config_params['map_positions'][map_pos_idx][2]]
            # calculate where in each environmental effect we are

            img_ctr += 1  # increment the image counter after a successful move

        elif blank_screenshot.exists() and not blank_screenshot.is_dir():
            img_moved = False
            while not img_moved:
                try:
                    shutil.move(blank_screenshot, Path(os.path.expanduser('~\\Documents\\SyntheticDataGen\\' + str(blank_ctr) + '_blank.png')))
                except OSError as e:
                    if e.errno == 13:
                        # print('File move error caught with OSError.errno 13') #  for debugging
                        # This sleep could be 0.2 secs but I don't want to use this high a sleep time.
                        # Could be an issue if the user makes the camera rotation time too low
                        time.sleep(0.1)
                        continue
                    # raise the exception if it is not this particular error
                    print('ERROR:')
                    print('The image file mover process has encountered some unknown error. Please restart the script.')
                    print('See the python error description here:')
                    print(e)
                    exit(4)
                # explicitly raise any other exception type
                except Exception as weirdE:
                    print('ERROR:')
                    print('The image file mover process has encountered some unknown error. Please restart the script.')
                    print('See the python error description here:')
                    print(weirdE)
                    exit(4)
                img_moved = True
            blank_ctr += 1  # increment the image counter after a successful move
        time.sleep(check_delay)  # sleep for check_delay seconds so we don't hammer the cpu unnecessarily
