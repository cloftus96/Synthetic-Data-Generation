"""  function: arma3_script_generator

     details: creates a .sqf file in the specified path, then writes script lines to the file which
              are arma 3 functions

     parameters: pos - an array of coordinates for the camera to move to
                 cc - time in between each screenshot
                 angle - the angle between each screenshot (angle x number of loop iterations = 360) """

import os
from pathlib import Path

def arma3_script_generator(map_pos, vehicle_name, pos, cc, angle):

    try:
        f = open('C:\\Program Files (x86)\\Steam\\steamapps\\common\\Arma 3\\Data_Generator.sqf', "w+")
    except Exception:
        print('ERROR:')
        print('Issue opening the Data_Generator.sqf file. See arma3_script_generator function.')
        exit(3)

    f.write('0 = [] spawn\n')
    f.write('{\n')
    f.write('_currentVehicle = "%s" createVehicle [%d, %d, %d];\n' % (vehicle_name, map_pos[0], map_pos[1], map_pos[2]))
    f.write('createVehicleCrew _currentVehicle;\n')
    f.write('_currentVehicle setdir 0;\n')
    f.write('_currentVehicle setVehiclePosition [_currentVehicle, [], 0];\n')
    f.write('pos1 = _currentVehicle modelToWorld [0,5,5];\n')
    f.write('cam = "camera" camCreate pos1;\n')
    f.write('cam cameraEffect ["INTERNAL", "BACK"];\n\n')
    f.write('angleface = 0;\n')
    f.write('fogvalue = 0;\n')
    f.write('angle = %d;\n\n' % angle)
    # top loop vehicle positions
    # next is vehicles
    # next is environments (fog, rain, time of day)
    # last is angles
    f.write('\twhile {fogvalue < .8} do\n')
    f.write('\t{\n')
    f.write('\t\twhile {angleface < 360} do\n')
    f.write('\t\t{\n')

    for idx, val in enumerate(pos):
        f.write('\t\t\tpos%d = pos%d vectorAdd [%d,%d,%d];\n' % (idx + 2, idx +1, pos[idx][0], pos[idx][1], pos[idx][2]))
        f.write('\t\t\tcam camSetPos pos%s;\n' % str(int(idx)+2))
        f.write('\t\t\tcam camSetTarget _currentVehicle;\n')
        f.write('\t\t\tcam camCommit %d;\n' % cc)
        f.write('\t\t\twaitUntil {camCommitted cam};\n')
        f.write('\t\t\tscreenshot "arma3screenshot.png";\n\n')
    f.write('\t\t\tangleface = angleface+angle;\n')
    f.write('\t\t\t{_currentVehicle deleteVehicleCrew _x} forEach crew _currentVehicle;\n')
    f.write('\t\t\tdeleteVehicle _currentVehicle;\n')
    f.write('\t\t\tsleep %d;\n' % cc)
    f.write('\t\t\t_currentVehicle = "%s" createVehicle [%d, %d, %d];\n' % (vehicle_name, map_pos[0], map_pos[1], map_pos[2]))
    f.write('\t\t\tcreateVehicleCrew _currentVehicle;\n')
    f.write('\t\t\t_currentVehicle setdir angleface;\n')
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


def create_mission_dir():
    """ This function creates the directory and files necessary to run our script as a mission. This includes putting
    a new folder in the default Arma 3 missions folder, as well as providing a default mission file and an init file
    that points to our script (this causes our script to run immediately upon playing the mission. """
    missionsFolder = Path(os.path.expanduser('~\\Documents\\Arma 3\\missions'))
    customMission = Path(str(missionsFolder) + '\\DataGeneration.Altis')
    if not customMission.exists():
        os.mkdir(customMission, 0o777)
    initfilepath = Path(str(customMission) + '\\init.sqf')
    missionfilepath = Path(str(customMission) + '\\mission.sqm')

    # write the init.sqf file
    initfile = open(initfilepath, "w+")
    initfile.write('execVM "Data_Generator.sqf";')
    initfile.close()

    # write the mission.sqm file
    missionfile = open(missionfilepath, "w+")
    missionfile.write('version=53')
    missionfile.write('class EditorData')
    missionfile.write('{')
    missionfile.write('\tmoveGridStep=1;')
    missionfile.write('\tangleGridStep=0.2617994;')
    missionfile.write('\tscaleGridStep=1;')
    missionfile.write('\tautoGroupingDist=10;')
    missionfile.write('\ttoggles=1;')
    missionfile.write('\tclass Camera')
    missionfile.write('\t{')
    missionfile.write('\t\tpos[]={14305.279,24.621294,17587.59};')
    missionfile.write('\t\tdir[]={-0.31484151,-0.17364819,-0.93312436};')
    missionfile.write('\t\tup[]={-0.055515055,0.98480767,-0.164535};')
    missionfile.write('\t\taside[]={-0.94751924,0,0.31969842};')
    missionfile.write('\t};')
    missionfile.write('};')
    missionfile.write('binarizationWanted=0;')
    missionfile.write('class AddonsMetaData')
    missionfile.write('{\n};')
    missionfile.write('randomSeed=8484358;')
    missionfile.write('class ScenarioData')
    missionfile.write('{\n\tauthor="";\n};')
