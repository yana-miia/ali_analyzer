from __future__ import print_function
import time
import ast
import aliseeksapi
from aliseeksapi.rest import ApiException
from pprint import pprint
from product import Product

configuration = aliseeksapi.Configuration()
configuration.api_key['X-API-CLIENT-ID'] = "RYXLKDJMKVVQZOXO"



def form_product(product_diction):
    """
    Form product from given dictionary.
    Additional function for avoiding copypaste code.
    """
    if product_diction["seller"]["total_feedback"] == 0:
        rating = 0
    else:
        rating = round(product_diction["seller"]["positive_feedback"]/\
                            product_diction["seller"]["total_feedback"]*100,2)

    product = Product(product_diction["id"],
                      product_diction["title"],
                      product_diction["category_id"],
                      product_diction["price"]["value"],
                      product_diction["freight"]["price"]["value"],
                      product_diction["price"]["currency"],
                      product_diction["orders"],
                      product_diction["seller"]["store_name"],
                      rating)
    return product



def get_best_sellings(category_id=None):
    """
    Get best selling list in chosen category.
    If you don't set category_id, it will find best selling in all categories.
    """
    api_instance = aliseeksapi.SearchApi(aliseeksapi.ApiClient(configuration))
    search_request = aliseeksapi.SearchRequest(sort="ORDERS",
                                            category=category_id,
                                            sort_direction='DESC')

    try:
        api_response = api_instance.search(search_request)
        buffer = ast.literal_eval(str(api_response))["items"]
        result = []
        for diction in buffer:
            if diction["title"] != None and diction["title"] != "":
                product = form_product(diction)
                result.append(product)
        return result


    except ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
        return None



def get_details_about_product(product_name):
    """
    Get detailed information about a product.
    """
    api_instance = aliseeksapi.SearchApi(aliseeksapi.ApiClient(configuration))
    search_request = aliseeksapi.SearchRequest(text=product_name,
                                            sort="BEST_MATCH",
                                            order_range={"from": 50},
                                            sort_direction='DESC',
                                            limit=50)
    try:
        api_response = api_instance.search(search_request)
        buffer = ast.literal_eval(str(api_response))["items"]
        converted_response = {}

        for diction in buffer:
            if diction["title"] != None and diction["title"] != "":
                product = form_product(diction)
                converted_response[product.seller_name] = \
                                {"price":product.price, "orders":product.orders}
        return converted_response
    except ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
        return None




if __name__ == "__main__":
    for i in get_best_sellings(100003070):
        print(i)
    print("\n\n\n")
    pprint(get_details_about_product("phone charger"))
