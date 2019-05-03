# aliseeksapi.ProductsApi

All URIs are relative to *https://api.aliseeks.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_product**](ProductsApi.md#get_product) | **POST** /products | Get products details as an aggregated request from AliExpress in realtime. 
[**get_product_details**](ProductsApi.md#get_product_details) | **POST** /products/details | Gets product details from AliExpress in realtime. 
[**get_product_html_description**](ProductsApi.md#get_product_html_description) | **POST** /products/description/html | Get product HTML description from AliExpress in realtime. 
[**get_product_shipping**](ProductsApi.md#get_product_shipping) | **POST** /products/shipping | Gets product shipping information AliExpress in realtime. 
[**get_product_skus**](ProductsApi.md#get_product_skus) | **POST** /products/variations | Gets product skus / variation information from AliExpress in realtime. 


# **get_product**
> Product get_product(product_request=product_request)

Get products details as an aggregated request from AliExpress in realtime. 

### Example

* Api Key Authentication (ApiKeyAuth): 
```python
from __future__ import print_function
import time
import aliseeksapi
from aliseeksapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = aliseeksapi.Configuration()
configuration.api_key['X-API-CLIENT-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-CLIENT-ID'] = 'Bearer'

# create an instance of the API class
api_instance = aliseeksapi.ProductsApi(aliseeksapi.ApiClient(configuration))
product_request = aliseeksapi.ProductRequest() # ProductRequest | The request body of get product  (optional)

try:
    # Get products details as an aggregated request from AliExpress in realtime. 
    api_response = api_instance.get_product(product_request=product_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_request** | [**ProductRequest**](ProductRequest.md)| The request body of get product  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_details**
> ProductDetail get_product_details(product_details_request)

Gets product details from AliExpress in realtime. 

### Example

* Api Key Authentication (ApiKeyAuth): 
```python
from __future__ import print_function
import time
import aliseeksapi
from aliseeksapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = aliseeksapi.Configuration()
configuration.api_key['X-API-CLIENT-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-CLIENT-ID'] = 'Bearer'

# create an instance of the API class
api_instance = aliseeksapi.ProductsApi(aliseeksapi.ApiClient(configuration))
product_details_request = aliseeksapi.ProductDetailsRequest() # ProductDetailsRequest | The request body to get product details 

try:
    # Gets product details from AliExpress in realtime. 
    api_response = api_instance.get_product_details(product_details_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_details_request** | [**ProductDetailsRequest**](ProductDetailsRequest.md)| The request body to get product details  | 

### Return type

[**ProductDetail**](ProductDetail.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_html_description**
> ProductHtmlDescription get_product_html_description(product_html_description_request)

Get product HTML description from AliExpress in realtime. 

### Example

* Api Key Authentication (ApiKeyAuth): 
```python
from __future__ import print_function
import time
import aliseeksapi
from aliseeksapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = aliseeksapi.Configuration()
configuration.api_key['X-API-CLIENT-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-CLIENT-ID'] = 'Bearer'

# create an instance of the API class
api_instance = aliseeksapi.ProductsApi(aliseeksapi.ApiClient(configuration))
product_html_description_request = aliseeksapi.ProductHtmlDescriptionRequest() # ProductHtmlDescriptionRequest | The request body to get product html description 

try:
    # Get product HTML description from AliExpress in realtime. 
    api_response = api_instance.get_product_html_description(product_html_description_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_html_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_html_description_request** | [**ProductHtmlDescriptionRequest**](ProductHtmlDescriptionRequest.md)| The request body to get product html description  | 

### Return type

[**ProductHtmlDescription**](ProductHtmlDescription.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_shipping**
> ProductShipping get_product_shipping(product_shipping_request)

Gets product shipping information AliExpress in realtime. 

### Example

* Api Key Authentication (ApiKeyAuth): 
```python
from __future__ import print_function
import time
import aliseeksapi
from aliseeksapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = aliseeksapi.Configuration()
configuration.api_key['X-API-CLIENT-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-CLIENT-ID'] = 'Bearer'

# create an instance of the API class
api_instance = aliseeksapi.ProductsApi(aliseeksapi.ApiClient(configuration))
product_shipping_request = aliseeksapi.ProductShippingRequest() # ProductShippingRequest | The request body to get product shipping 

try:
    # Gets product shipping information AliExpress in realtime. 
    api_response = api_instance.get_product_shipping(product_shipping_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_shipping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_shipping_request** | [**ProductShippingRequest**](ProductShippingRequest.md)| The request body to get product shipping  | 

### Return type

[**ProductShipping**](ProductShipping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_skus**
> ProductSkus get_product_skus(product_skus_request)

Gets product skus / variation information from AliExpress in realtime. 

### Example

* Api Key Authentication (ApiKeyAuth): 
```python
from __future__ import print_function
import time
import aliseeksapi
from aliseeksapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = aliseeksapi.Configuration()
configuration.api_key['X-API-CLIENT-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-CLIENT-ID'] = 'Bearer'

# create an instance of the API class
api_instance = aliseeksapi.ProductsApi(aliseeksapi.ApiClient(configuration))
product_skus_request = aliseeksapi.ProductSkusRequest() # ProductSkusRequest | The request body to get product skus / variations 

try:
    # Gets product skus / variation information from AliExpress in realtime. 
    api_response = api_instance.get_product_skus(product_skus_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_skus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_skus_request** | [**ProductSkusRequest**](ProductSkusRequest.md)| The request body to get product skus / variations  | 

### Return type

[**ProductSkus**](ProductSkus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

