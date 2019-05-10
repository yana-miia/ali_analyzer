from user import User
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
