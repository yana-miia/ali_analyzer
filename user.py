class User:
    """
    Represents a user.
    Base class for Seller and Buyer.
    """
    main_categories = {
        "Apparel for women": 100003109,
        "Apparel for men": 100003070,
        "Cellphones & Telecommunications": 509,
        "Computer & Office": 7,
        "Consumer Electronics": 44,
        "Jewelry & Accessories": 1509,
        "Home & Garden": 15,
        "Luggage & Bags": 1524,
        "Shoes": 322,
        "Mother & Kids": 1501,
        "Sports & Entertainment": 18,
        "Beauty & Health": 66,
        "Watches": 1511,
        "Toys & Hobbies": 26,
        "Weddings & Events": 100003235,
        "Novelty & Special Use": 200000875,
        "Automobiles & Motorcycles": 34,
        "Lights & Lighting": 39,
        "Furniture": 1503,
        "Electronic Components & Supplies": 502,
        "Office & School": 21,
        "Home Appliances Parts": 100000016,
        "Home Improvement": 13,
        "Security & Protection": 30,
        "Tools": 1420,
        "Hair Extensions & Wigs": 200002489
    }

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
