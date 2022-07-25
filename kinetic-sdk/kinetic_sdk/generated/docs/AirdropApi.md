# openapi_client.AirdropApi

All URIs are relative to *https://devnet.kinetic.kin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**airdrop_stats**](AirdropApi.md#airdrop_stats) | **GET** /api/airdrop/stats | 
[**request_airdrop**](AirdropApi.md#request_airdrop) | **POST** /api/airdrop | 


# **airdrop_stats**
> AirdropStats airdrop_stats()



### Example


```python
import time
import openapi_client
from openapi_client.api import airdrop_api
from openapi_client.model.airdrop_stats import AirdropStats
from pprint import pprint
# Defining the host is optional and defaults to https://devnet.kinetic.kin.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://devnet.kinetic.kin.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = airdrop_api.AirdropApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 
        api_response = api_instance.airdrop_stats()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AirdropApi->airdrop_stats: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AirdropStats**](AirdropStats.md)

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

# **request_airdrop**
> RequestAirdropResponse request_airdrop(request_airdrop_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import airdrop_api
from openapi_client.model.request_airdrop_response import RequestAirdropResponse
from openapi_client.model.request_airdrop_request import RequestAirdropRequest
from pprint import pprint
# Defining the host is optional and defaults to https://devnet.kinetic.kin.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://devnet.kinetic.kin.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = airdrop_api.AirdropApi(api_client)
    request_airdrop_request = RequestAirdropRequest(
        account="account_example",
        amount="amount_example",
        commitment="Confirmed",
        environment="environment_example",
        index=1,
        mint="mint_example",
    ) # RequestAirdropRequest | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.request_airdrop(request_airdrop_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AirdropApi->request_airdrop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_airdrop_request** | [**RequestAirdropRequest**](RequestAirdropRequest.md)|  |

### Return type

[**RequestAirdropResponse**](RequestAirdropResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

