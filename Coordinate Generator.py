def coords(in1, in2):
    import math
    length = 100
    angle = 270
    radangle = math.radians(angle)
    new_x = length * math.cos(radangle)
    new_y = length * math.sin(radangle)
    x = '%.3f'%(new_x)
    y ='%.3f'%(new_y)
    print(x)
    print(y)
    return (x, y)