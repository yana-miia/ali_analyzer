from user import User


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

    def get_id(self):
        """
        Return the id of thge buyer.
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
    buyer.get_comands()
