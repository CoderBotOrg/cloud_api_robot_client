import typing_extensions

from cloud_api_robot_client.paths import PathValues
from cloud_api_robot_client.apis.paths.robot_data import RobotData
from cloud_api_robot_client.apis.paths.robot_setting import RobotSetting
from cloud_api_robot_client.apis.paths.robot_activities import RobotActivities
from cloud_api_robot_client.apis.paths.robot_programs import RobotPrograms

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ROBOT_DATA: RobotData,
        PathValues.ROBOT_SETTING: RobotSetting,
        PathValues.ROBOT_ACTIVITIES: RobotActivities,
        PathValues.ROBOT_PROGRAMS: RobotPrograms,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ROBOT_DATA: RobotData,
        PathValues.ROBOT_SETTING: RobotSetting,
        PathValues.ROBOT_ACTIVITIES: RobotActivities,
        PathValues.ROBOT_PROGRAMS: RobotPrograms,
    }
)
