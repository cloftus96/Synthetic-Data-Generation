def coords(in1, in2, in3):
    import math
    length = in1
    angle = in2
    radangle = math.radians(angle)
    new_x = length * math.cos(radangle)
    new_y = length * math.sin(radangle)
    x = float('%.3f'%(new_x))
    y = float('%.3f'%(new_y))
    #print(x)
    #print(y)
    return (int(x), int(y), in3)
