# kinetic_sdk_generated.TransactionApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_latest_blockhash**](TransactionApi.md#get_latest_blockhash) | **GET** /api/transaction/latest-blockhash/{environment}/{index} | 
[**get_minimum_rent_exemption_balance**](TransactionApi.md#get_minimum_rent_exemption_balance) | **GET** /api/transaction/minimum-rent-exemption-balance/{environment}/{index} | 
[**get_transaction**](TransactionApi.md#get_transaction) | **GET** /api/transaction/transaction/{environment}/{index}/{signature} | 
[**make_transfer**](TransactionApi.md#make_transfer) | **POST** /api/transaction/make-transfer | 


# **get_latest_blockhash**
> LatestBlockhashResponse get_latest_blockhash(environment, index)



### Example


```python
import time
import kinetic_sdk_generated
from kinetic_sdk_generated.api import transaction_api
from kinetic_sdk_generated.model.latest_blockhash_response import LatestBlockhashResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = kinetic_sdk_generated.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with kinetic_sdk_generated.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)
    environment = "environment_example" # str | 
    index = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_latest_blockhash(environment, index)
        pprint(api_response)
    except kinetic_sdk_generated.ApiException as e:
        print("Exception when calling TransactionApi->get_latest_blockhash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**|  |
 **index** | **int**|  |

### Return type

[**LatestBlockhashResponse**](LatestBlockhashResponse.md)

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

# **get_minimum_rent_exemption_balance**
> MinimumRentExemptionBalanceResponse get_minimum_rent_exemption_balance(environment, index, data_length)



### Example


```python
import time
import kinetic_sdk_generated
from kinetic_sdk_generated.api import transaction_api
from kinetic_sdk_generated.model.minimum_rent_exemption_balance_response import MinimumRentExemptionBalanceResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = kinetic_sdk_generated.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with kinetic_sdk_generated.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)
    environment = "environment_example" # str | 
    index = 1 # int | 
    data_length = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_minimum_rent_exemption_balance(environment, index, data_length)
        pprint(api_response)
    except kinetic_sdk_generated.ApiException as e:
        print("Exception when calling TransactionApi->get_minimum_rent_exemption_balance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**|  |
 **index** | **int**|  |
 **data_length** | **int**|  |

### Return type

[**MinimumRentExemptionBalanceResponse**](MinimumRentExemptionBalanceResponse.md)

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

# **get_transaction**
> GetTransactionResponse get_transaction(environment, index, signature)



### Example


```python
import time
import kinetic_sdk_generated
from kinetic_sdk_generated.api import transaction_api
from kinetic_sdk_generated.model.get_transaction_response import GetTransactionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = kinetic_sdk_generated.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with kinetic_sdk_generated.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)
    environment = "environment_example" # str | 
    index = 1 # int | 
    signature = "signature_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_transaction(environment, index, signature)
        pprint(api_response)
    except kinetic_sdk_generated.ApiException as e:
        print("Exception when calling TransactionApi->get_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**|  |
 **index** | **int**|  |
 **signature** | **str**|  |

### Return type

[**GetTransactionResponse**](GetTransactionResponse.md)

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

# **make_transfer**
> Transaction make_transfer(make_transfer_request)



### Example


```python
import time
import kinetic_sdk_generated
from kinetic_sdk_generated.api import transaction_api
from kinetic_sdk_generated.model.transaction import Transaction
from kinetic_sdk_generated.model.make_transfer_request import MakeTransferRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = kinetic_sdk_generated.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with kinetic_sdk_generated.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)
    make_transfer_request = MakeTransferRequest(
        commitment=Commitment("Confirmed"),
        environment="environment_example",
        index=1,
        mint="mint_example",
        last_valid_block_height=1,
        reference_id="reference_id_example",
        reference_type="reference_type_example",
        tx="tx_example",
    ) # MakeTransferRequest | 

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.make_transfer(make_transfer_request)
        pprint(api_response)
    except kinetic_sdk_generated.ApiException as e:
        print("Exception when calling TransactionApi->make_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **make_transfer_request** | [**MakeTransferRequest**](MakeTransferRequest.md)|  |

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

