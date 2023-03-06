import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.coder_bot_cloud_api_api import CoderBotCloudAPIApi
from openapi_client.apis.tags.robot_sync_api import RobotSyncApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CODER_BOT_CLOUD_API: CoderBotCloudAPIApi,
        TagValues.ROBOTSYNC: RobotSyncApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CODER_BOT_CLOUD_API: CoderBotCloudAPIApi,
        TagValues.ROBOTSYNC: RobotSyncApi,
    }
)
