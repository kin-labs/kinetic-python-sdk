# openapi_client.AppApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_config**](AppApi.md#get_app_config) | **GET** /api/app/{environment}/{index}/config | 
[**get_app_health**](AppApi.md#get_app_health) | **GET** /api/app/{environment}/{index}/health | 


# **get_app_config**
> AppConfig get_app_config(environment, index)



### Example


```python
import time
import openapi_client
from openapi_client.api import app_api
from openapi_client.model.app_config import AppConfig
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = app_api.AppApi(api_client)
    environment = "environment_example" # str | 
    index = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_app_config(environment, index)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AppApi->get_app_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**|  |
 **index** | **int**|  |

### Return type

[**AppConfig**](AppConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_health**
> AppHealth get_app_health(environment, index)



### Example


```python
import time
import openapi_client
from openapi_client.api import app_api
from openapi_client.model.app_health import AppHealth
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = app_api.AppApi(api_client)
    environment = "environment_example" # str | 
    index = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_app_health(environment, index)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AppApi->get_app_health: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**|  |
 **index** | **int**|  |

### Return type

[**AppHealth**](AppHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

