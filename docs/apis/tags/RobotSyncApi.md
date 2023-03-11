<a name="__pageTop"></a>
# cloud_api_robot_client.apis.tags.robot_sync_api.RobotSyncApi

All URIs are relative to *https://api.coderbot.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_robot_activities**](#get_robot_activities) | **get** /robot/activities | Get robot activities
[**get_robot_data**](#get_robot_data) | **get** /robot/data | Get robot data
[**get_robot_programs**](#get_robot_programs) | **get** /robot/programs | Get robot programs
[**get_robot_setting**](#get_robot_setting) | **get** /robot/setting | Get robot data
[**set_robot_activities**](#set_robot_activities) | **put** /robot/activities | Set robot settings
[**set_robot_programs**](#set_robot_programs) | **put** /robot/programs | Put robot programs
[**set_robot_setting**](#set_robot_setting) | **put** /robot/setting | Set robot settings
[**update_robot_data**](#update_robot_data) | **put** /robot/data | Update CoderBot data

# **get_robot_activities**
<a name="get_robot_activities"></a>
> [Activity] get_robot_activities()

Get robot activities

Get CoderBot current activities

### Example

* Bearer Authentication (coderbot_auth):
```python
import cloud_api_robot_client
from cloud_api_robot_client.apis.tags import robot_sync_api
from cloud_api_robot_client.model.activity import Activity
from pprint import pprint
# Defining the host is optional and defaults to https://api.coderbot.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = cloud_api_robot_client.Configuration(
    host = "https://api.coderbot.org/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: coderbot_auth
configuration = cloud_api_robot_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with cloud_api_robot_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = robot_sync_api.RobotSyncApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get robot activities
        api_response = api_instance.get_robot_activities()
        pprint(api_response)
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->get_robot_activities: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_robot_activities.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_robot_activities.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#get_robot_activities.ApiResponseFor405) | Invalid input

#### get_robot_activities.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Activity**]({{complexTypePrefix}}Activity.md) | [**Activity**]({{complexTypePrefix}}Activity.md) | [**Activity**]({{complexTypePrefix}}Activity.md) |  | 

#### get_robot_activities.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_robot_activities.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_robot_data**
<a name="get_robot_data"></a>
> Robot get_robot_data()

Get robot data

Get CoderBot current configuration

### Example

* Bearer Authentication (coderbot_auth):
```python
import cloud_api_robot_client
from cloud_api_robot_client.apis.tags import robot_sync_api
from cloud_api_robot_client.model.robot import Robot
from pprint import pprint
# Defining the host is optional and defaults to https://api.coderbot.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = cloud_api_robot_client.Configuration(
    host = "https://api.coderbot.org/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: coderbot_auth
configuration = cloud_api_robot_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with cloud_api_robot_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = robot_sync_api.RobotSyncApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get robot data
        api_response = api_instance.get_robot_data()
        pprint(api_response)
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->get_robot_data: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_robot_data.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_robot_data.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#get_robot_data.ApiResponseFor405) | Invalid input

#### get_robot_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Robot**](../../models/Robot.md) |  | 


#### get_robot_data.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_robot_data.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_robot_programs**
<a name="get_robot_programs"></a>
> [Program] get_robot_programs()

Get robot programs

Get CoderBot current programs

### Example

* Bearer Authentication (coderbot_auth):
```python
import cloud_api_robot_client
from cloud_api_robot_client.apis.tags import robot_sync_api
from cloud_api_robot_client.model.program import Program
from pprint import pprint
# Defining the host is optional and defaults to https://api.coderbot.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = cloud_api_robot_client.Configuration(
    host = "https://api.coderbot.org/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: coderbot_auth
configuration = cloud_api_robot_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with cloud_api_robot_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = robot_sync_api.RobotSyncApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get robot programs
        api_response = api_instance.get_robot_programs()
        pprint(api_response)
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->get_robot_programs: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_robot_programs.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_robot_programs.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#get_robot_programs.ApiResponseFor405) | Invalid input

#### get_robot_programs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Program**]({{complexTypePrefix}}Program.md) | [**Program**]({{complexTypePrefix}}Program.md) | [**Program**]({{complexTypePrefix}}Program.md) |  | 

#### get_robot_programs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_robot_programs.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_robot_setting**
<a name="get_robot_setting"></a>
> Setting get_robot_setting()

Get robot data

Get CoderBot current setting

### Example

* Bearer Authentication (coderbot_auth):
```python
import cloud_api_robot_client
from cloud_api_robot_client.apis.tags import robot_sync_api
from cloud_api_robot_client.model.setting import Setting
from pprint import pprint
# Defining the host is optional and defaults to https://api.coderbot.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = cloud_api_robot_client.Configuration(
    host = "https://api.coderbot.org/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: coderbot_auth
configuration = cloud_api_robot_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with cloud_api_robot_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = robot_sync_api.RobotSyncApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get robot data
        api_response = api_instance.get_robot_setting()
        pprint(api_response)
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->get_robot_setting: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_robot_setting.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_robot_setting.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#get_robot_setting.ApiResponseFor405) | Invalid input

#### get_robot_setting.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Setting**](../../models/Setting.md) |  | 


#### get_robot_setting.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_robot_setting.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_robot_activities**
<a name="set_robot_activities"></a>
> set_robot_activities(activity)

Set robot settings

Set CoderBot current activities

### Example

* Bearer Authentication (coderbot_auth):
```python
import cloud_api_robot_client
from cloud_api_robot_client.apis.tags import robot_sync_api
from cloud_api_robot_client.model.activity import Activity
from pprint import pprint
# Defining the host is optional and defaults to https://api.coderbot.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = cloud_api_robot_client.Configuration(
    host = "https://api.coderbot.org/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: coderbot_auth
configuration = cloud_api_robot_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with cloud_api_robot_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = robot_sync_api.RobotSyncApi(api_client)

    # example passing only required values which don't have defaults set
    body = [
        Activity(
            id="10",
            org_id="10",
            name="Learn movement",
            description="First grade students, CoderBot primer",
            data="{}",
            modified="2017-07-21T17:32:28Z",
            status="active",
        )
    ]
    try:
        # Set robot settings
        api_response = api_instance.set_robot_activities(
            body=body,
        )
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->set_robot_activities: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Activity**]({{complexTypePrefix}}Activity.md) | [**Activity**]({{complexTypePrefix}}Activity.md) | [**Activity**]({{complexTypePrefix}}Activity.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_robot_activities.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#set_robot_activities.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#set_robot_activities.ApiResponseFor405) | Invalid input

#### set_robot_activities.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### set_robot_activities.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### set_robot_activities.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_robot_programs**
<a name="set_robot_programs"></a>
> set_robot_programs()

Put robot programs

Get CoderBot current programs

### Example

* Bearer Authentication (coderbot_auth):
```python
import cloud_api_robot_client
from cloud_api_robot_client.apis.tags import robot_sync_api
from cloud_api_robot_client.model.program import Program
from pprint import pprint
# Defining the host is optional and defaults to https://api.coderbot.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = cloud_api_robot_client.Configuration(
    host = "https://api.coderbot.org/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: coderbot_auth
configuration = cloud_api_robot_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with cloud_api_robot_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = robot_sync_api.RobotSyncApi(api_client)

    # example passing only optional values
    body = [
        Program(
            id="10",
            org_id="10",
            name="Obstacle avoidance",
            description="An Obstacle avoidance demo",
            code="code_example",
            dom_code="dom_code_example",
            modified="2017-07-21T17:32:28Z",
            status="active",
        )
    ]
    try:
        # Put robot programs
        api_response = api_instance.set_robot_programs(
            body=body,
        )
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->set_robot_programs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Program**]({{complexTypePrefix}}Program.md) | [**Program**]({{complexTypePrefix}}Program.md) | [**Program**]({{complexTypePrefix}}Program.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_robot_programs.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#set_robot_programs.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#set_robot_programs.ApiResponseFor405) | Invalid input

#### set_robot_programs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### set_robot_programs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### set_robot_programs.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_robot_setting**
<a name="set_robot_setting"></a>
> set_robot_setting(setting)

Set robot settings

Get CoderBot current setting

### Example

* Bearer Authentication (coderbot_auth):
```python
import cloud_api_robot_client
from cloud_api_robot_client.apis.tags import robot_sync_api
from cloud_api_robot_client.model.setting import Setting
from pprint import pprint
# Defining the host is optional and defaults to https://api.coderbot.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = cloud_api_robot_client.Configuration(
    host = "https://api.coderbot.org/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: coderbot_auth
configuration = cloud_api_robot_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with cloud_api_robot_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = robot_sync_api.RobotSyncApi(api_client)

    # example passing only required values which don't have defaults set
    body = Setting(
        id="10",
        org_id="10",
        name="EnglishSlow",
        description="English locale, Slow movements",
        data="{}",
        modified="2017-07-21T17:32:28Z",
        status="active",
    )
    try:
        # Set robot settings
        api_response = api_instance.set_robot_setting(
            body=body,
        )
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->set_robot_setting: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Setting**](../../models/Setting.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_robot_setting.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#set_robot_setting.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#set_robot_setting.ApiResponseFor405) | Invalid input

#### set_robot_setting.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### set_robot_setting.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### set_robot_setting.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_robot_data**
<a name="update_robot_data"></a>
> update_robot_data(robot)

Update CoderBot data

Update CoderBot data

### Example

* Bearer Authentication (coderbot_auth):
```python
import cloud_api_robot_client
from cloud_api_robot_client.apis.tags import robot_sync_api
from cloud_api_robot_client.model.robot import Robot
from pprint import pprint
# Defining the host is optional and defaults to https://api.coderbot.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = cloud_api_robot_client.Configuration(
    host = "https://api.coderbot.org/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: coderbot_auth
configuration = cloud_api_robot_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with cloud_api_robot_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = robot_sync_api.RobotSyncApi(api_client)

    # example passing only required values which don't have defaults set
    body = Robot(
        id="10",
        org_id="10",
        name="CoderBot123",
        description="The CoderBot 123",
        setting="setting_example",
        activities=[
            "activities_example"
        ],
,
        status="active",
    )
    try:
        # Update CoderBot data
        api_response = api_instance.update_robot_data(
            body=body,
        )
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->update_robot_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Robot**](../../models/Robot.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_robot_data.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#update_robot_data.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#update_robot_data.ApiResponseFor405) | Invalid input

#### update_robot_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_robot_data.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_robot_data.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

