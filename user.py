from ali_requests import get_best_sellings

class User:
    """
    Represents a user.
    Base class for Seller and Buyer.
    """
    main_categories = {
        "All":None,
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
        "Furniture": 1503,
        "Electronic Components & Supplies": 502,
        "Office & School": 21,
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
        self.commands = {"best products": "Show you the bestselling products."}


    def get_best_products(self, category="All"):
        """
        Get list of bestselling products in chosen category, sorted with chosen
        sorting way.
        """
        category_id = User.main_categories[category]
        list_of_bests = get_best_sellings(category_id)
        return list_of_bests


    def __str__(self):
        result = ''
        for command in self.commands:
            result += command + " --> " + self.commands[command] + '\n'
        return 'Commands of ' + self.nickname + ':\n\n' + result


if __name__ == '__main__':
    user = User("Wall-e")
    user.print_commands()
