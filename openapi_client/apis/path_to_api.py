import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.robot_data import RobotData
from openapi_client.apis.paths.robot_setting import RobotSetting
from openapi_client.apis.paths.robot_activities import RobotActivities
from openapi_client.apis.paths.robot_programs import RobotPrograms

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
