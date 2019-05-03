# aliseeksapi.SearchApi

All URIs are relative to *https://api.aliseeks.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realtime_search**](SearchApi.md#realtime_search) | **POST** /search/realtime | Searches AliExpress in realtime 
[**search**](SearchApi.md#search) | **POST** /search | Searches AliExpress in non-realtime. Uses the Aliseeks.com datasource which is continually updated from AliExpress. 
[**search_best_selling**](SearchApi.md#search_best_selling) | **POST** /search/bestSelling | Retrieves best selling products from AliExpress in realtime. 
[**search_by_image**](SearchApi.md#search_by_image) | **POST** /search/image | Searches AliExpress by image in realtime. 
[**upload_image_by_url**](SearchApi.md#upload_image_by_url) | **POST** /search/image/upload | Uploads an image to AliExpress to allow it to be used in the image search endpoint 


# **realtime_search**
> RealtimeSearchResponse realtime_search(realtime_search_request)

Searches AliExpress in realtime 

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
api_instance = aliseeksapi.SearchApi(aliseeksapi.ApiClient(configuration))
realtime_search_request = aliseeksapi.RealtimeSearchRequest() # RealtimeSearchRequest | Realtime search request body 

try:
    # Searches AliExpress in realtime 
    api_response = api_instance.realtime_search(realtime_search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->realtime_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realtime_search_request** | [**RealtimeSearchRequest**](RealtimeSearchRequest.md)| Realtime search request body  | 

### Return type

[**RealtimeSearchResponse**](RealtimeSearchResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResponse search(search_request)

Searches AliExpress in non-realtime. Uses the Aliseeks.com datasource which is continually updated from AliExpress. 

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
api_instance = aliseeksapi.SearchApi(aliseeksapi.ApiClient(configuration))
search_request = aliseeksapi.SearchRequest() # SearchRequest | Search request body 

try:
    # Searches AliExpress in non-realtime. Uses the Aliseeks.com datasource which is continually updated from AliExpress. 
    api_response = api_instance.search(search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)| Search request body  | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_best_selling**
> BestSellingSearchResponse search_best_selling(best_selling_search_request)

Retrieves best selling products from AliExpress in realtime. 

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
api_instance = aliseeksapi.SearchApi(aliseeksapi.ApiClient(configuration))
best_selling_search_request = aliseeksapi.BestSellingSearchRequest() # BestSellingSearchRequest | Search best selling request body 

try:
    # Retrieves best selling products from AliExpress in realtime. 
    api_response = api_instance.search_best_selling(best_selling_search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_best_selling: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **best_selling_search_request** | [**BestSellingSearchRequest**](BestSellingSearchRequest.md)| Search best selling request body  | 

### Return type

[**BestSellingSearchResponse**](BestSellingSearchResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_by_image**
> ImageSearchResponse search_by_image(image_search_request)

Searches AliExpress by image in realtime. 

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
api_instance = aliseeksapi.SearchApi(aliseeksapi.ApiClient(configuration))
image_search_request = aliseeksapi.ImageSearchRequest() # ImageSearchRequest | The image search request body 

try:
    # Searches AliExpress by image in realtime. 
    api_response = api_instance.search_by_image(image_search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_by_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_search_request** | [**ImageSearchRequest**](ImageSearchRequest.md)| The image search request body  | 

### Return type

[**ImageSearchResponse**](ImageSearchResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_image_by_url**
> UploadImageResponse upload_image_by_url(upload_image_by_url_request)

Uploads an image to AliExpress to allow it to be used in the image search endpoint 

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
api_instance = aliseeksapi.SearchApi(aliseeksapi.ApiClient(configuration))
upload_image_by_url_request = aliseeksapi.UploadImageByUrlRequest() # UploadImageByUrlRequest | The upload image by url request body 

try:
    # Uploads an image to AliExpress to allow it to be used in the image search endpoint 
    api_response = api_instance.upload_image_by_url(upload_image_by_url_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->upload_image_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_image_by_url_request** | [**UploadImageByUrlRequest**](UploadImageByUrlRequest.md)| The upload image by url request body  | 

### Return type

[**UploadImageResponse**](UploadImageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

