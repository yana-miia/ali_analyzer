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

    def names_of_best_products(self, category=None):
        """
        Get list of bestselling products in chosen category, sorted with chosen
        sorting way.
        """
        category_id = Seller.main_categories[category]
        list_of_bests = get_best_sellings(category_id)
        return list_of_bests

if __name__ == '__main__':
    seller = Seller("Solomiia")
    seller.get_comands()
    for i in seller.names_of_best_products("Shoes"):
        print(i)
    print("\n\n\n")
    pprint(Seller.main_categories)
