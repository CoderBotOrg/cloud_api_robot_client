# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from cloud_api_robot_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ROBOT_REGISTER = "/robot/register"
    ROBOT_DATA = "/robot/data"
    ROBOT_SETTING = "/robot/setting"
    ROBOT_ACTIVITIES = "/robot/activities"
    ROBOT_ACTIVITIES_ACTIVITY_ID = "/robot/activities/{activity_id}"
    ROBOT_PROGRAMS = "/robot/programs"
    ROBOT_PROGRAMS_PROGRAM_ID = "/robot/programs/{program_id}"
