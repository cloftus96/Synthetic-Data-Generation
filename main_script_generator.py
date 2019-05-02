import Coordinate_Generator
import Basic_Script_Writing
import sys


def position_generator(angle_step, x_init, cam_z_val):
    # maybe do error/type checking on the inputs later...
    curr_angle = 0
    # default_cc = 2  # can take this as an argument if we want ||| removed for now
    pos_array = []
    while curr_angle < 360:
        pos_array.append(Coordinate_Generator.coords(x_init, curr_angle, cam_z_val))
        curr_angle += angle_step
    return pos_array


def generate_script(map_pos, vehicle_names, fog_increment, time_increment, pos_array, rota_angle_step):
    default_cc = 2
    Basic_Script_Writing.arma3_script_generator(map_pos, vehicle_names, fog_increment, time_increment, pos_array, default_cc, rota_angle_step)

