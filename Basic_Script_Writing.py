#*******************************************************************************************************
#
#     function: arma3_script_generator
#
#     details: creates a .sqf file in the specified path, then writes script lines to the file which
#              are arma 3 functions
#
#     parameters: pos - an array of coordinates for the camera to move to
#                 cc - time in between each screenshot
#                 angle - the angle between each screenshot
#
#*******************************************************************************************************

def arma3_script_generator(pos, cc, angle):
    f = open('C:\\Program Files (x86)\\Steam\\steamapps\\common\\Arma 3\\Data_Generator.sqf', "w+")
    f.write('_currentVehicle = "armaNameofVehicle" createVehicle [mapPositionCoordX, mapPositionCoordY, 0];\n')
    f.write('createVehicleCrew _currentVehicle;\n')
    f.write('_currentVehicle setdir 0;\n')
    f.write('_currentVehicle setVehiclePosition [_currentVehicle, [], 0];\n')
    f.write('pos1 = _currentVehicle modelToWorld [0,5,5];\n')
    f.write('cam = "camera" camCreate pos1;\n')
    f.write('cam cameraEffect ["INTERNAL", "BACK"];\n\n')
    f.write('angleface = 0;\n')
    f.write('fogvalue = 0;\n')
    f.write('angle = %d;\n\n' % angle)
    f.write('0 = [] spawn\n')
    f.write('{\n')
    # top loop vehicle positions
    # next is vehicles
    # next is environments (fog, rain, time of day)
    # last is angles
    f.write('\twhile {fogvalue < .8} do\n')
    f.write('\t{\n')
    f.write('\t\twhile {angleface < 360} do\n')
    f.write('\t\t{\n')
    f.write('\t\t\twaitUntil {camCommitted cam};\n')
    f.write('\t\t\tscreenshot "arma3screenshot.png";\n')
    for idx, val in enumerate(pos):
        f.write('\t\t\tpos%d = player modelToWorld [%d,%d,%d];\n' % (idx + 2, pos[idx][0], pos[idx][1], pos[idx][2]))
        f.write('\t\t\tcam camSetPos pos%s;\n' % str(int(idx)+2))
        f.write('\t\t\tcam camSetDir (pos%s vectorFromTo pos1);\n' % str(int(idx)+2))
        f.write('\t\t\tcam camCommit %d;\n' % cc)
        f.write('\t\t\twaitUntil {camCommitted cam};\n')
        f.write('\t\t\tscreenshot "arma3screenshot.png";\n\n')
    f.write('\t\t\tangleface = angleface+angle;\n')
    f.write('\t\t\tforEach crew _createVehicle;\n')
    f.write('\t\t\tdeleteVehicle _currentVehicle;\n')
    f.write('\t\t\t_currentVehicle = "armaNameofVehicle" createVehicle [mapPositionCoordX, mapPositionCoordY, 0];\n')
    f.write('\t\t\tcreateVehicleCrew _currentVehicle;\n')
    f.write('\t\t\t_currentVehicle setdir angleface\n;')
    f.write('\t\t\t_currentVehicle setVehiclePosition [_currentVehicle, [], 0];\n')
    f.write('\t\t\tsleep %d;\n' % cc)
    f.write('\t\t};\n')
    f.write('\tfogvalue = fogvalue + .2;\n')
    f.write('\t1 setfog fogvalue;\n')
    f.write('\tsleep %d;\n' % cc)
    f.write('\tangleface = 0;\n')
    f.write('\t};\n')
    f.write('};\n')
    f.close()
