
from __future__ import print_function
import time
import aliseeksapi
from aliseeksapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = aliseeksapi.Configuration()
configuration.api_key['X-API-CLIENT-ID'] = "RYXLKDJMKVVQZOXO"
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-CLIENT-ID'] = 'Bearer'
api_instance = aliseeksapi.SearchApi(aliseeksapi.ApiClient(configuration))
search_request = aliseeksapi.SearchRequest(sort="ORDERS", currency="USD", category=100003070) # SearchRequest | Search request body

try:
    # Searches AliExpress in non-realtime. Uses the Aliseeks.com datasource which is continually updated from AliExpress.
    api_response = api_instance.search(search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)
