import Coordinate_Generator
import Basic_Script_Writing
def main(angle_step, x_init):
    # maybe do error/type checking on the inputs later...
    curr_angle = angle_step
    default_cc = 2
    pos_array = []
    idx = 0
    while curr_angle < 360:
        pos_array[idx] = Coordinate_Generator.coords(x_init, curr_angle, 100)
        curr_angle += angle_step
        idx += 1
    Basic_Script_Writing.script(pos_array, len(pos_array)+2, default_cc)

if __name__ == "__main__":
    main()
