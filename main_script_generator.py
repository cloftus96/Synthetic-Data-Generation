import Coordinate_Generator
import Basic_Script_Writing
import sys


def position_generator(angle_step, x_init, rota_angle_step):
    # maybe do error/type checking on the inputs later...
    curr_angle = 0
    default_cc = 2  # can take this as an argument if we want
    pos_array = []
    while curr_angle < 360:
        pos_array.append(Coordinate_Generator.coords(x_init, curr_angle, 100))
        curr_angle += angle_step
    Basic_Script_Writing.script(pos_array, default_cc, rota_angle_step)


if __name__ == "__main__":
    #  probably do not need this assert?
    assert len(sys.argv) > 3, "Angle step, x-distance from center, and platform rotation angle step required as inputs"
    position_generator(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
