from user import User
from ratings import Ratings, SellerRatings, BuyerRatings
from ali_requests import get_best_sellings, search_products
from pprint import pprint


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
        self.commands.update({"best products":"Show you the bestselling " \
            "products.", \
            "best sellers":"Gives you list of best sellers with their rating.",\
            "worst sellers":"Gives you the list of worst sellers.",
            "best shipping":"Shows you the market with chosen product, where " \
            "the speed of shipping is the highest.",
            "alternative":"Gives you options for buying alternative products."})


    def get_best_sellers(self, category="All"):
        """
        Find Best Sellers in chosen category according to their ratings.
        It gives our buyer the opportunity to find best options for buying
        products.
        """
        best_sellers = []
        for product in self.get_best_products(category):
            best_sellers.append(product.seller_name)
        return best_sellers


    def get_worst_sellers(self, category = "ALL"):
        """
        Find Best Sellers in chosen category according to their ratings.
        It gives our buyer the opportunity to avoid bad options for buying
        products.
        """
        worst_sellers = []
        # not implemented yet


    def get_alternative(self, product_name):
        """
        Return the list of alternative products.
        """
        products = search_products(product_name)
        alternatives = []
        for product in products:
            for i in range(len(products) - 1):
                for j in range(len(products) - 2):
                    if products[i].product_id == products[j].product_id:
                        alternatives.append(products[i])
        return alternatives


    def find_best_shipping(product_id):
        """
        """
        # not implemented yet


    def get_ratings(self):
        """
        Return the instance of BuyerRatings class, which contains all details
        about the ratings.
        """
        # not implemented yet


# if __name__ == '__main__':
#     buyer = Buyer("Yana")
#     print(buyer)
    #print("Best sellers in the category:")
    #pprint(buyer.get_best_sellers())
