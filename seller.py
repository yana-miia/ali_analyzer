from user import User
from ALI import get_best_sellings
from pprint import pprint

class Seller(User):
    """
    Represent a seller.
    Subclass of User.
    """

    def __init__(self, nickname):
        """
        Initialize a seller.
        """
        super().__init__(nickname)
        self.comand_list = ["search", "analyze"]

    def names_of_best_products(self, sort_way, category_id):
        """
        Get list og bestselling products in chosen category, sorted with chosen
        sorting way.
        """
        list_of_bests = []
        for item in get_best_sellings(sort_way, category_id):
            list_of_bests.append(item['title'])
        return list_of_bests

if __name__ == '__main__':
    seller = Seller("Solomiia")
    seller.get_comands()
    pprint(seller.names_of_best_products("ORDERS", 100003070))
