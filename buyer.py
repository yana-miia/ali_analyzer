from user import User
from ali_requests import get_best_sellings, search_products, \
    search_similar_products, get_product_info_by_id, get_shipping
from pprint import pprint

def short_title(title):
    """
    Function to shorten string of the title of the product.
    """
    lst = title.split()
    lst1 = []
    lst1.append(lst[0])
    lst1.append(lst[1])
    lst1.append(lst[2])
    lst1.append(lst[3])
    lst1.append(lst[4])
    lst1.append(lst[5])
    lst1.append(lst[6])
    lst1.append(lst[7])
    prod_name = " ".join(lst1)
    return prod_name


class Buyer(User):
    """
    Represent a buyer.
    Subclass of User.
    """

    def __init__(self, nickname):
        """
        Initialize a buyer.
        """
        super().__init__(nickname)
        self.commands.update({"1 - best products":"Show you the bestselling " \
            "products.", \
            "2 - best sellers":"Gives you list of best sellers with their rating.",\
            "3 - worst sellers":"Gives you the list of worst sellers.",
            "4 - best shipping":"Shows you the market with chosen product, where " \
            "the speed of shipping is the highest.",
            "5 - alternative":"Gives you options for buying alternative products."})


    def get_best_sellers(self, category="All"):
        """
        Find Best Sellers in chosen category according to their product's
        ratings. It gives our buyer the opportunity to find best options for
        buying products.
        """
        best_sellers = []
        for product in self.get_best_products(category):
            best_sellers.append(product.seller_name)
        return best_sellers


    def get_worst_sellers(self, category = "ALL"):
        """
        Find Worst Sellers in chosen category according to their product's
        ratings. It gives our buyer the opportunity to avoid bad options for
        buying products.
        """
        worst_sellers = []
        for product in self.get_worst_products(category):
            worst_sellers.append(product.seller_name)
        return worst_sellers


    def get_alternative(self, product_id):
        """
        Return the list of alternative products.
        """
        product = get_product_info_by_id(product_id)
        print("Alternatives for ", short_title(product.title),
        " from category ", product.category_id, ":")
        alternatives = search_similar_products(product.title,\
            product.category_id)
        for alternative in alternatives:
            print((short_title(alternative.title), alternative.seller_name))
        for prod in alternatives:
            if prod.product_id == product_id:
                alternatives.remove(prod)
        return alternatives


    def find_best_shipping(self, product_name):
        """
        Get shipping speed of given product.
        """
        products = search_products(product_name)
        result = []
        for prod in products:
            result.append((prod.seller_name, get_shipping(prod.product_id)))
        return result
