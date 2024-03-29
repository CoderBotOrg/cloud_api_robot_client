# cloud_api_robot_client.model.activity.Activity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  | Organization id | [optional] 
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**data** | str,  | str,  |  | [optional] 
**kind** | str,  | str,  | Activity kind | [optional] must be one of ["stock", "user", ] 
**modified** | str,  | str,  |  | [optional] 
**status** | str,  | str,  | Activity status | [optional] must be one of ["active", "deactivated", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

