class User:
    """
    Represents a user.
    Base class for Seller and Buyer.
    """

    def __init__(self, nickname):
        """
        Initialize a user.
        """
        self.nickname = nickname
        self.command_list = []

    def get_comands(self):
        print(self.command_list)


if __name__ == '__main__':
    user = User("Wall-e")
    user.get_comands()
