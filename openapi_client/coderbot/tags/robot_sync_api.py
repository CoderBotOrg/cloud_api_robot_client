# coding: utf-8

"""
    CoderBot Cloud API - Robot only - OpenAPI 3.0

    CoderBot Cloud API - Robot only  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: info@coderbot.org
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.robot_activities.get import GetRobotActivities
from openapi_client.paths.robot_data.get import GetRobotData
from openapi_client.paths.robot_programs.get import GetRobotPrograms
from openapi_client.paths.robot_setting.get import GetRobotSetting
from openapi_client.paths.robot_activities.put import SetRobotActivities
from openapi_client.paths.robot_programs.put import SetRobotPrograms
from openapi_client.paths.robot_setting.put import SetRobotSetting
from openapi_client.paths.robot_data.put import UpdateRobotData


class RobotSyncApi(
    GetRobotActivities,
    GetRobotData,
    GetRobotPrograms,
    GetRobotSetting,
    SetRobotActivities,
    SetRobotPrograms,
    SetRobotSetting,
    UpdateRobotData,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
