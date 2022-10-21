# kinetic_sdk_generated.AccountApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](AccountApi.md#create_account) | **POST** /api/account/create | 
[**get_account_info**](AccountApi.md#get_account_info) | **GET** /api/account/info/{environment}/{index}/{accountId} | 
[**get_balance**](AccountApi.md#get_balance) | **GET** /api/account/balance/{environment}/{index}/{accountId} | 
[**get_history**](AccountApi.md#get_history) | **GET** /api/account/history/{environment}/{index}/{accountId}/{mint} | 
[**get_token_accounts**](AccountApi.md#get_token_accounts) | **GET** /api/account/token-accounts/{environment}/{index}/{accountId}/{mint} | 


# **create_account**
> Transaction create_account(create_account_request)



### Example


```python
import time
import kinetic_sdk_generated
from kinetic_sdk_generated.api import account_api
from kinetic_sdk_generated.model.transaction import Transaction
from kinetic_sdk_generated.model.create_account_request import CreateAccountRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = kinetic_sdk_generated.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with kinetic_sdk_generated.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    create_account_request = CreateAccountRequest(
        commitment=Commitment("Confirmed"),
        environment="environment_example",
        index=1,
        last_valid_block_height=1,
        mint="mint_example",
        reference_id="reference_id_example",
        reference_type="reference_type_example",
        tx="tx_example",
    ) # CreateAccountRequest | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.create_account(create_account_request)
        pprint(api_response)
    except kinetic_sdk_generated.ApiException as e:
        print("Exception when calling AccountApi->create_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_account_request** | [**CreateAccountRequest**](CreateAccountRequest.md)|  |

### Return type

[**Transaction**](Transaction.md)

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

# **get_account_info**
> get_account_info(environment, index, account_id)



### Example


```python
import time
import kinetic_sdk_generated
from kinetic_sdk_generated.api import account_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = kinetic_sdk_generated.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with kinetic_sdk_generated.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    environment = "environment_example" # str | 
    index = 1 # int | 
    account_id = "accountId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_instance.get_account_info(environment, index, account_id)
    except kinetic_sdk_generated.ApiException as e:
        print("Exception when calling AccountApi->get_account_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**|  |
 **index** | **int**|  |
 **account_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance**
> BalanceResponse get_balance(environment, index, account_id)



### Example


```python
import time
import kinetic_sdk_generated
from kinetic_sdk_generated.api import account_api
from kinetic_sdk_generated.model.balance_response import BalanceResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = kinetic_sdk_generated.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with kinetic_sdk_generated.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    environment = "environment_example" # str | 
    index = 1 # int | 
    account_id = "accountId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_balance(environment, index, account_id)
        pprint(api_response)
    except kinetic_sdk_generated.ApiException as e:
        print("Exception when calling AccountApi->get_balance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**|  |
 **index** | **int**|  |
 **account_id** | **str**|  |

### Return type

[**BalanceResponse**](BalanceResponse.md)

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

# **get_history**
> [HistoryResponse] get_history(environment, index, account_id, mint)



### Example


```python
import time
import kinetic_sdk_generated
from kinetic_sdk_generated.api import account_api
from kinetic_sdk_generated.model.history_response import HistoryResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = kinetic_sdk_generated.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with kinetic_sdk_generated.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    environment = "environment_example" # str | 
    index = 1 # int | 
    account_id = "accountId_example" # str | 
    mint = "mint_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_history(environment, index, account_id, mint)
        pprint(api_response)
    except kinetic_sdk_generated.ApiException as e:
        print("Exception when calling AccountApi->get_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**|  |
 **index** | **int**|  |
 **account_id** | **str**|  |
 **mint** | **str**|  |

### Return type

[**[HistoryResponse]**](HistoryResponse.md)

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

# **get_token_accounts**
> [str] get_token_accounts(environment, index, account_id, mint)



### Example


```python
import time
import kinetic_sdk_generated
from kinetic_sdk_generated.api import account_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = kinetic_sdk_generated.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with kinetic_sdk_generated.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    environment = "environment_example" # str | 
    index = 1 # int | 
    account_id = "accountId_example" # str | 
    mint = "mint_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_token_accounts(environment, index, account_id, mint)
        pprint(api_response)
    except kinetic_sdk_generated.ApiException as e:
        print("Exception when calling AccountApi->get_token_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**|  |
 **index** | **int**|  |
 **account_id** | **str**|  |
 **mint** | **str**|  |

### Return type

**[str]**

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

