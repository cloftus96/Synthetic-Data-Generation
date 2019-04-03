import os.path
from pathlib import Path
import time
import shutil


def image_file_mover(check_delay):
    """ This function will check a pre-determined directory for pre-determined file name and will continue to check,
    sleeping for <check_delay> seconds between each check. If the file exists, it will move it to a separate
    pre-determined directory. check_delay should be 1/2 the time it takes to rotate the camera to the next position.
    """
    img_ctr = 1
    done = False
    # check for file in ~/arma3/
    screenshot_path = Path(os.path.expanduser('~\\Documents\\Arma 3\\Screenshots'))
    dest_dir = Path(os.path.expanduser('~\\Documents\\SyntheticDataGen'))
    if not Path.exists(dest_dir):
        os.makedirs(str(dest_dir), 0o777)  # create the directory if it doesnt exist
    # if not screenshot_path.exists(): # I will fix this later
        # need to do some error stuff here
    while not done:
        screenshot = Path(str(screenshot_path) + '\\arma3screenshot.png')
        if screenshot.exists() and not screenshot.is_dir():
            # exit with error code 4 if this fails...
            img_moved = False
            while not img_moved:
                try:
                    shutil.move(screenshot, Path(os.path.expanduser('~\\Documents\\SyntheticDataGen\\' + str(img_ctr) + '.png')))
                except OSError as e:
                    if e.errno == 13:
                        # print('File move error caught with OSError.errno 13') #  for debugging
                        continue
                    # raise the exception if it is not this particular error
                    raise
                # explicitly raise any other exception type
                except Exception:
                    raise
                img_moved = True
            img_ctr += 1  # increment the image counter after a successful move
        time.sleep(check_delay)  # sleep for check_delay seconds so we don't hammer the cpu unnecessarily
