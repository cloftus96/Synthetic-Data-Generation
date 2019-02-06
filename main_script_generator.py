import Coordinate_Generator
import Basic_Script_Writing
import sys


def position_generator(angle_step, x_init):
    # maybe do error/type checking on the inputs later...
    curr_angle = angle_step  # we do not need to start at zero. See basic_script_writing
    default_cc = 2  # can take this as an argument if we want
    pos_array = []
    while curr_angle < 360:
        pos_array.append(Coordinate_Generator.coords(x_init, curr_angle, 100))
        curr_angle += angle_step
    Basic_Script_Writing.script(pos_array, len(pos_array) + 2, default_cc)


if __name__ == "__main__":
    assert len(sys.argv) > 2, "Angle step and x-distance from center required as inputs"
    position_generator(int(sys.argv[1]), int(sys.argv[2]))
