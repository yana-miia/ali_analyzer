from user import User
from ratings import Ratings, SellerRatings, BuyerRatings
from ALI import get_best_sellings, search_products
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
        self.comand_list = ["find", "comparate"]


    def __str__(self):
        result = ''
        for i in self.comand_list:
            result += i + '\n'
        return 'Commands of ' + self.nickname + ':\n' + result


    def get_best_products(self, category="All"):
        """
        Get list of bestselling products in chosen category, sorted with chosen
        sorting way.
        """
        category_id = Seller.main_categories[category]
        list_of_bests = get_best_sellings(category_id)
        return list_of_bests


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
    print(str(buyer))
