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
        self.command_list.extend(["find",
                                  "comparate"])


    def get_best_sellers(self, category="All"):
        """
        Find Best Sellers in chosen category according to their ratings.
        It gives our buyer the opportunity to find best options for buying products.
        """
        best_sellers = []
        for product in self.get_best_products(category):
            best_sellers.append(product.seller_name)
        return best_sellers


    def get_id(self):
        """
        Return the id of the buyer.
        """

    def get_ratings(self):
        """
        Return the instance of BuyerRatings class, which contains all details about
        the ratings.
        """

    def get_order_history(self):
        """
        Return the list of shops where the buyer made orders.
        """


if __name__ == '__main__':
    buyer = Buyer("Yana")
    print(buyer)
    #print("Best sellers in the category:")
    #pprint(buyer.get_best_sellers())
