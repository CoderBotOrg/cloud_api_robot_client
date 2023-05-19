import typing_extensions

from cloud_api_robot_client.paths import PathValues
from cloud_api_robot_client.apis.paths.robot_register import RobotRegister
from cloud_api_robot_client.apis.paths.robot_data import RobotData
from cloud_api_robot_client.apis.paths.robot_setting import RobotSetting
from cloud_api_robot_client.apis.paths.robot_activities import RobotActivities
from cloud_api_robot_client.apis.paths.robot_activities_activity_id import RobotActivitiesActivityId
from cloud_api_robot_client.apis.paths.robot_programs import RobotPrograms
from cloud_api_robot_client.apis.paths.robot_programs_program_id import RobotProgramsProgramId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ROBOT_REGISTER: RobotRegister,
        PathValues.ROBOT_DATA: RobotData,
        PathValues.ROBOT_SETTING: RobotSetting,
        PathValues.ROBOT_ACTIVITIES: RobotActivities,
        PathValues.ROBOT_ACTIVITIES_ACTIVITY_ID: RobotActivitiesActivityId,
        PathValues.ROBOT_PROGRAMS: RobotPrograms,
        PathValues.ROBOT_PROGRAMS_PROGRAM_ID: RobotProgramsProgramId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ROBOT_REGISTER: RobotRegister,
        PathValues.ROBOT_DATA: RobotData,
        PathValues.ROBOT_SETTING: RobotSetting,
        PathValues.ROBOT_ACTIVITIES: RobotActivities,
        PathValues.ROBOT_ACTIVITIES_ACTIVITY_ID: RobotActivitiesActivityId,
        PathValues.ROBOT_PROGRAMS: RobotPrograms,
        PathValues.ROBOT_PROGRAMS_PROGRAM_ID: RobotProgramsProgramId,
    }
)
