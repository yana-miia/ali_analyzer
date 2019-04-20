from user import User


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

    def get_id(self):
        """
        Return the id of the seller.
        """
    def get_shops(self):
        """
        Get the list of shops where the seller is trading.
        """
    def get_ratings(self):
        """
        Return the instance of SellerRatings class, which contains all details about
        the ratings.
        """


if __name__ == '__main__':
    seller = Seller("Solomiia")
    seller.get_comands()
