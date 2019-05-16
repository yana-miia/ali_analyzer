from __future__ import print_function
import time
import ast
import aliseeksapi
from aliseeksapi.rest import ApiException
from pprint import pprint
from product import Product, DetailedProduct

configuration = aliseeksapi.Configuration()
configuration.api_key['X-API-CLIENT-ID'] = "YOUR_API"


def form_product(product_diction):
    """
    Form Product from given dictionary.
    Additional function for avoiding repeating code.
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


def form_detailed_product(product_diction):
    """
    Form DetailedProduct from given dictionary.
    Additional function for avoiding repeating code.
    """
    min_price = product_diction["prices"][0]["min_amount"]["value"]
    max_price = product_diction["prices"][0]["max_amount"]["value"]

    product = DetailedProduct(product_diction["id"],
                        product_diction["title"],
                        product_diction["category_id"],
                        (min_price + max_price)/2,
                        'No Info',
                        product_diction["prices"][0]["min_amount"]["currency"],
                        product_diction["trade"]["sold"],
                        "-", "-",
                        min_price, max_price,
                        product_diction["wish_list_count"])
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
        print("Error when calling SearchApi->get_best_sellings: %s\n" % e)
        return None


def search_products(product_name):
    """
    Get detailed information about some type of  a product.
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
        result = []
        for diction in buffer:
            if diction["title"] != None and diction["title"] != "":
                product = form_product(diction)
                result.append(product)
        return result

    except ApiException as e:
        print("Error when calling SearchApi->search_products: %s\n" % e)
        return None


def get_product_info_by_id(product_id):
    """
    Get details about one product by it's id.
    """
    api_instance = aliseeksapi.ProductsApi(aliseeksapi.ApiClient(configuration))
    search_request = aliseeksapi.ProductRequest(product_id=product_id)
    try:
        api_response = api_instance.get_product_details(search_request)
        buffer = ast.literal_eval(str(api_response))
        return form_detailed_product(buffer)

    except ApiException as e:
        print("Error when calling ProductApi->get_product_info_by_id: %s\n" % e)
        return None

#uncomment blocks to test some function
if __name__ == "__main__":
    #for i in get_best_sellings(100003070):
    #    print(i)
    #print("\n\n\n")

    #pprint(search_products("phone charger"))

    print(get_product_info_by_id(32826890025))
