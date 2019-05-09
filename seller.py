from user import User
from ALI import get_best_sellings, search_products
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

    def get_best_products(self, category="All"):
        """
        Get list of bestselling products in chosen category, sorted with chosen
        sorting way.
        """
        category_id = Seller.main_categories[category]
        list_of_bests = get_best_sellings(category_id)
        return list_of_bests

    def find_demand(self):
        """
        Find demand on each category in bestselling.
        """
        demand = {}
        for category in Seller.main_categories:
            if category == "All":
                continue
            buffer = self.get_best_products(category)
            amount_of_orders = 0
            for product in buffer:
                amount_of_orders += product.orders
            demand[category] = int(amount_of_orders)
        return sorted(demand.items(), key=lambda x: x[1], reverse = True)

    def get_best_sellers(self, category="All"):
        """
        Find Best Sellers in chosen category.
        """
        best_sellers = []
        for product in self.get_best_products(category):
            best_sellers.append(product.seller_name)
        return best_sellers


    def get_product_statistic(self, product_name):
        """
        Return statistic about product selling.
        """
        statistic = {}
        for product in search_products(product_name):
            statistic[product.seller_name] = \
                                {"price":product.price, "orders":product.orders}
        return statistic



if __name__ == '__main__':
    seller = Seller("Solomiia")

    #print("Best Selling:")
    #for i in seller.get_best_products():
    #    print(i)
    #print("\n\n\n")

    #print("Demand:")
    #pprint(seller.find_demand())
    #print("\n\n\n")

    #print("Best Sellers:")
    #pprint(seller.get_best_sellers())
    #print("\n\n\n")

    #print("Statistic about 'phone charger':")
    #pprint(seller.get_product_statistic('phone charger'))
    #print("\n\n\n")
