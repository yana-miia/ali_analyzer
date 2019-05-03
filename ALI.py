from __future__ import print_function
import time
import ast
import aliseeksapi
from aliseeksapi.rest import ApiException
from pprint import pprint
from product import Product
# Configure API key authorization: ApiKeyAuth
configuration = aliseeksapi.Configuration()
configuration.api_key['X-API-CLIENT-ID'] = "RYXLKDJMKVVQZOXO"
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-CLIENT-ID'] = 'Bearer'
def get_best_sellings(sort_way, category_id):
    api_instance = aliseeksapi.SearchApi(aliseeksapi.ApiClient(configuration))
    search_request = aliseeksapi.SearchRequest(sort=sort_way, category=category_id) # SearchRequest | Search request body

    try:
        # Searches AliExpress in non-realtime. Uses the Aliseeks.com datasource which is continually updated from AliExpress.
        api_response = api_instance.search(search_request)
        buffer = ast.literal_eval(str(api_response))["items"]
        result = []
        for diction in buffer:
            if diction["title"] != None and diction["title"] != "":
                product = Product(diction["title"],
                                  diction["category_id"],
                                  diction["price"]["value"],
                                  diction["freight"]["price"]["value"],
                                  diction["price"]["currency"],
                                  diction["seller"]["store_name"],
                                  round(diction["seller"]["positive_feedback"]/diction["seller"]["total_feedback"]*100,2))
                result.append(product)
        return result


    except ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
        return None

if __name__ == "__main__":
    for i in get_best_sellings("ORDERS", 100003070):
        print(i)
