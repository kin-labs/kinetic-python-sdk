# kinetic_sdk_generated.AirdropApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_airdrop**](AirdropApi.md#request_airdrop) | **POST** /api/airdrop | 


# **request_airdrop**
> RequestAirdropResponse request_airdrop(request_airdrop_request)



### Example


```python
import time
import kinetic_sdk_generated
from kinetic_sdk_generated.api import airdrop_api
from kinetic_sdk_generated.model.request_airdrop_request import RequestAirdropRequest
from kinetic_sdk_generated.model.request_airdrop_response import RequestAirdropResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = kinetic_sdk_generated.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with kinetic_sdk_generated.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = airdrop_api.AirdropApi(api_client)
    request_airdrop_request = RequestAirdropRequest(
        account="account_example",
        amount="amount_example",
        commitment=Commitment("Confirmed"),
        environment="environment_example",
        index=1,
        mint="mint_example",
    ) # RequestAirdropRequest | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.request_airdrop(request_airdrop_request)
        pprint(api_response)
    except kinetic_sdk_generated.ApiException as e:
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

