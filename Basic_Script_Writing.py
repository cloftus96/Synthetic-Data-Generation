"""  function: arma3_script_generator

     details: creates a .sqf file in the specified path, then writes script lines to the file which
              are arma 3 functions

     parameters: pos - an array of coordinates for the camera to move to
                 cc - time in between each screenshot
                 angle - the angle between each screenshot (angle x number of loop iterations = 360) """

import os
from pathlib import Path


def arma3_script_generator(map_pos, vehicle_name, fog_increment, time_increment, pos, cc, angle):

    try:
        f = open(str(Path(os.path.expanduser('~\\Documents\\Arma 3\\missions\\DataGeneration.Stratis\\briefing.sqf'))), 'w+')
    except Exception:
        print('ERROR:')
        print('Issue opening the Data_Generator.sqf file. See arma3_script_generator function.')
        exit(3)

    f.write('0 = [] spawn\n')
    f.write('{\n')
    f.write('skipTime (6 - daytime + 24 ) % 24;\n')
    f.write('0 setFog 0;\n')
    f.write('0 setOvercast 0;\n')
    f.write('0 setRain 0;\n')
    f.write('_currentVehicle = "%s" createVehicle [%d, %d, %d];\n' % (vehicle_name, map_pos[0], map_pos[1], map_pos[2]))
    f.write('createVehicleCrew _currentVehicle;\n')
    f.write('_currentVehicle setdir 0;\n')
    f.write('_currentVehicle setVehiclePosition [_currentVehicle, [], 0];\n')
    f.write('pos1 = _currentVehicle modelToWorld [0,5,5];\n')
    f.write('cam = "camera" camCreate pos1;\n')
    f.write('cam cameraEffect ["INTERNAL", "BACK"];\n\n')
    f.write('angleface = 0;\n')
    f.write('fogvalue = 0;\n')
    f.write('timevalue = 6;\n')
    f.write('angle = %d;\n\n' % angle)
    # top loop vehicle positions
    # next is vehicles
    # next is environments (fog, rain, time of day)
    # last is angles
    f.write('\twhile {timevalue < 19.5} do\n')
    f.write('\t{\n')
    f.write('\t\twhile {fogvalue < .8} do\n')
    f.write('\t\t{\n')
    f.write('\t\t\twhile {angleface < 360} do\n')
    f.write('\t\t\t{\n')

    for idx, val in enumerate(pos):
        f.write('\t\t\t\tpos%d = pos1 vectorAdd [%d,%d,%d];\n' % (idx + 2, pos[idx][0], pos[idx][1], pos[idx][2]))
        f.write('\t\t\t\tcam camSetPos pos%s;\n' % str(int(idx)+2))
        f.write('\t\t\t\tcam camSetTarget _currentVehicle;\n')
        f.write('\t\t\t\tcam camCommit %d;\n' % cc)
        f.write('\t\t\t\twaitUntil {camCommitted cam};\n')
        f.write('\t\t\t\tscreenshot "arma3screenshot.png";\n\n')
    f.write('\t\t\t\tangleface = angleface+angle;\n')
    f.write('\t\t\t\t{_currentVehicle deleteVehicleCrew _x} forEach crew _currentVehicle;\n')
    f.write('\t\t\t\tdeleteVehicle _currentVehicle;\n')
    f.write('\t\t\t\tsleep %d;\n' % cc)
    f.write('\t\t\t\t_currentVehicle = "%s" createVehicle [%d, %d, %d];\n' % (vehicle_name, map_pos[0], map_pos[1], map_pos[2]))
    f.write('\t\t\t\tcreateVehicleCrew _currentVehicle;\n')
    f.write('\t\t\t\t_currentVehicle setdir angleface;\n')
    f.write('\t\t\t\t_currentVehicle setVehiclePosition [_currentVehicle, [], 0];\n')
    f.write('\t\t\t\tsleep %d;\n' % cc)
    f.write('\t\t\t};\n')
    f.write('\t\tfogvalue = fogvalue + %d;\n' % fog_increment)
    f.write('\t\t1 setFog fogvalue;\n')
    f.write('\t\tsleep %d;\n' % cc)
    f.write('\t\tangleface = 0;\n')
    f.write('\t\t};\n')
    f.write('\ttimevalue = timevalue + %d;\n' % time_increment)
    f.write('\tskipTime (timevalue - daytime + 24 ) % 24;\n')
    f.write('\t0 setFog 0;\n')
    f.write('\t0 setOvercast 0;\n')
    f.write('\t0 setRain 0;\n')
    f.write('\tfogvalue = 0;\n')
    f.write('\tsleep %d;\n' % cc)
    f.write('\t};\n')
    f.write('};\n')
    f.close()


def create_mission_dir():
    """
        function name: create_mission_dir

        details: This function creates the directory and files necessary to run our script as a mission. This includes putting
    a new folder in the default Arma 3 missions folder, as well as providing a default mission file and an init file
    that points to our script (this causes our script to run immediately upon playing the mission.

        parameters: none

    """
    missionsFolder = Path(os.path.expanduser('~\\Documents\\Arma 3\\missions'))
    customMission = Path(str(missionsFolder) + '\\DataGeneration.Stratis')
    print(customMission)
    if not customMission.exists():
        os.makedirs(customMission, 0o777)
    initfilepath = Path(str(customMission) + '\\init.sqf')
    missionfilepath = Path(str(customMission) + '\\mission.sqm')

    # write the init.sqf file
    initfile = open(initfilepath, "w+")
    initfile.write('execVM "briefing.sqf";')
    initfile.close()

    # write the mission.sqm file
    missionfile = open(missionfilepath, "w+")
    missionfile.write('version=53;\n')
    missionfile.write('class EditorData\n')
    missionfile.write('{\n')
    missionfile.write('\tmoveGridStep=1;\n')
    missionfile.write('\tangleGridStep=0.2617994;\n')
    missionfile.write('\tscaleGridStep=1;\n')
    missionfile.write('\tautoGroupingDist=10;\n')
    missionfile.write('\ttoggles=1;\n')
    missionfile.write('\tclass Camera\n')
    missionfile.write('\t{\n')
    missionfile.write('\t\tpos[]={14305.279,24.621294,17587.59};\n')
    missionfile.write('\t\tdir[]={-0.31484151,-0.17364819,-0.93312436};\n')
    missionfile.write('\t\tup[]={-0.055515055,0.98480767,-0.164535};\n')
    missionfile.write('\t\taside[]={-0.94751924,0,0.31969842};\n')
    missionfile.write('\t};\n')
    missionfile.write('};\n')
    missionfile.write('binarizationWanted=0;\n')
    missionfile.write('class AddonsMetaData\n')
    missionfile.write('{\n};\n')
    missionfile.write('randomSeed=8484358;\n')
    missionfile.write('class ScenarioData\n')
    missionfile.write('{\n\tauthor="";\n};')
