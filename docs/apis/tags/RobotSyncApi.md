<a name="__pageTop"></a>
# cloud_api_robot_client.apis.tags.robot_sync_api.RobotSyncApi

All URIs are relative to *https://api.coderbot.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_robot_activity**](#create_robot_activity) | **post** /robot/activities | Create a new robot activity
[**create_robot_program**](#create_robot_program) | **post** /robot/programs | Create new robot program
[**delete_robot_activity**](#delete_robot_activity) | **delete** /robot/activities/{activity_id} | Delete robot activity
[**delete_robot_program**](#delete_robot_program) | **delete** /robot/programs/{program_id} | Delete robot program
[**get_robot_activities**](#get_robot_activities) | **get** /robot/activities | Get robot activities
[**get_robot_data**](#get_robot_data) | **get** /robot/data | Get robot data
[**get_robot_programs**](#get_robot_programs) | **get** /robot/programs | Get robot programs
[**get_robot_setting**](#get_robot_setting) | **get** /robot/setting | Get robot data
[**set_robot_activity**](#set_robot_activity) | **put** /robot/activities/{activity_id} | Set robot activity
[**set_robot_program**](#set_robot_program) | **put** /robot/programs/{program_id} | Put robot program
[**set_robot_setting**](#set_robot_setting) | **put** /robot/setting | Set robot settings
[**update_robot_data**](#update_robot_data) | **put** /robot/data | Update CoderBot data

# **create_robot_activity**
<a name="create_robot_activity"></a>
> Activity create_robot_activity(activity)

Create a new robot activity

Create a new robot activity

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
    body = Activity(
        id="10",
        org_id="10",
        name="Learn movement",
        description="First grade students, CoderBot primer",
        data="{}",
        modified="2017-07-21T17:32:28Z",
        status="active",
    )
    try:
        # Create a new robot activity
        api_response = api_instance.create_robot_activity(
            body=body,
        )
        pprint(api_response)
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->create_robot_activity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Activity**](../../models/Activity.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_robot_activity.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#create_robot_activity.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#create_robot_activity.ApiResponseFor405) | Invalid input

#### create_robot_activity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Activity**](../../models/Activity.md) |  | 


#### create_robot_activity.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_robot_activity.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_robot_program**
<a name="create_robot_program"></a>
> Program create_robot_program(program)

Create new robot program

Create new robot program

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

    # example passing only required values which don't have defaults set
    body = Program(
        id="10",
        org_id="10",
        name="Obstacle avoidance",
        description="An Obstacle avoidance demo",
        code="code_example",
        dom_code="dom_code_example",
        modified="2017-07-21T17:32:28Z",
        status="active",
    )
    try:
        # Create new robot program
        api_response = api_instance.create_robot_program(
            body=body,
        )
        pprint(api_response)
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->create_robot_program: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Program**](../../models/Program.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_robot_program.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#create_robot_program.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#create_robot_program.ApiResponseFor405) | Invalid input

#### create_robot_program.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Program**](../../models/Program.md) |  | 


#### create_robot_program.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_robot_program.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_robot_activity**
<a name="delete_robot_activity"></a>
> delete_robot_activity(activity_id)

Delete robot activity

Delete CoderBot activity

### Example

* Bearer Authentication (coderbot_auth):
```python
import cloud_api_robot_client
from cloud_api_robot_client.apis.tags import robot_sync_api
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
    path_params = {
        'activity_id': "activity_id_example",
    }
    try:
        # Delete robot activity
        api_response = api_instance.delete_robot_activity(
            path_params=path_params,
        )
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->delete_robot_activity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
activity_id | ActivityIdSchema | | 

# ActivityIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_robot_activity.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#delete_robot_activity.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#delete_robot_activity.ApiResponseFor405) | Invalid input

#### delete_robot_activity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_robot_activity.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_robot_activity.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_robot_program**
<a name="delete_robot_program"></a>
> delete_robot_program(program_id)

Delete robot program

Delete CoderBot current program

### Example

* Bearer Authentication (coderbot_auth):
```python
import cloud_api_robot_client
from cloud_api_robot_client.apis.tags import robot_sync_api
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
    path_params = {
        'program_id': "program_id_example",
    }
    try:
        # Delete robot program
        api_response = api_instance.delete_robot_program(
            path_params=path_params,
        )
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->delete_robot_program: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
program_id | ProgramIdSchema | | 

# ProgramIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_robot_program.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#delete_robot_program.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#delete_robot_program.ApiResponseFor405) | Invalid input

#### delete_robot_program.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_robot_program.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_robot_program.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

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

# **set_robot_activity**
<a name="set_robot_activity"></a>
> Activity set_robot_activity(activity_idactivity)

Set robot activity

Set CoderBot activity

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
    path_params = {
        'activity_id': "activity_id_example",
    }
    body = Activity(
        id="10",
        org_id="10",
        name="Learn movement",
        description="First grade students, CoderBot primer",
        data="{}",
        modified="2017-07-21T17:32:28Z",
        status="active",
    )
    try:
        # Set robot activity
        api_response = api_instance.set_robot_activity(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->set_robot_activity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Activity**](../../models/Activity.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
activity_id | ActivityIdSchema | | 

# ActivityIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_robot_activity.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#set_robot_activity.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#set_robot_activity.ApiResponseFor405) | Invalid input

#### set_robot_activity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Activity**](../../models/Activity.md) |  | 


#### set_robot_activity.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### set_robot_activity.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[coderbot_auth](../../../README.md#coderbot_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_robot_program**
<a name="set_robot_program"></a>
> Program set_robot_program(program_idprogram)

Put robot program

Put CoderBot current program

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

    # example passing only required values which don't have defaults set
    path_params = {
        'program_id': "program_id_example",
    }
    body = Program(
        id="10",
        org_id="10",
        name="Obstacle avoidance",
        description="An Obstacle avoidance demo",
        code="code_example",
        dom_code="dom_code_example",
        modified="2017-07-21T17:32:28Z",
        status="active",
    )
    try:
        # Put robot program
        api_response = api_instance.set_robot_program(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->set_robot_program: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Program**](../../models/Program.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
program_id | ProgramIdSchema | | 

# ProgramIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_robot_program.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#set_robot_program.ApiResponseFor404) | Not found
405 | [ApiResponseFor405](#set_robot_program.ApiResponseFor405) | Invalid input

#### set_robot_program.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Program**](../../models/Program.md) |  | 


#### set_robot_program.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### set_robot_program.ApiResponseFor405
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
> Setting set_robot_setting(setting)

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
        pprint(api_response)
    except cloud_api_robot_client.ApiException as e:
        print("Exception when calling RobotSyncApi->set_robot_setting: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
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
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Setting**](../../models/Setting.md) |  | 


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

