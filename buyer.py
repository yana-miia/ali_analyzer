from user import User
from ali_requests import get_best_sellings, search_products, \
    search_similar_products, get_product_info_by_id
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
        self.commands.update({"1 - best products":"Show you the bestselling " \
            "products.", \
            "2 - best sellers":"Gives you list of best sellers with their rating.",\
            "3 - worst sellers":"Gives you the list of worst sellers.",
            "4 - best shipping":"Shows you the market with chosen product, where " \
            "the speed of shipping is the highest.",
            "5 - alternative":"Gives you options for buying alternative products."})


    def get_best_sellers(self, category="All"):
        """
        Find Best Sellers in chosen category according to their product's
        ratings. It gives our buyer the opportunity to find best options for
        buying products.
        """
        best_sellers = []
        for product in self.get_best_products(category):
            best_sellers.append(product.seller_name)
        return best_sellers


    def get_worst_sellers(self, category = "ALL"):
        """
        Find Worst Sellers in chosen category according to their product's
        ratings. It gives our buyer the opportunity to avoid bad options for
        buying products.
        """
        worst_sellers = []
        for product in self.get_worst_products(category):
            worst_sellers.append({product.seller_name: product.seller_rating})
        return worst_sellers


    def get_alternative(self, product_id):
        """
        Return the list of alternative products.
        """
        product = get_product_info_by_id(product_id)
        print("Looking for alternatives for ", product.title," from category ",\
            product.category_id)
        alternatives = search_similar_products(product.title,\
            product.category_id)
        print("Alternatives:\n", alternatives)
        for prod in alternatives:
            if prod.product_id == product_id:
                alternatives.remove(prod)
        return alternatives


    def find_best_shipping(product_id):
        """
        """
        # not implemented yet





# if __name__ == '__main__':
#     buyer = Buyer("Yana")
#     print(buyer)
    #print("Best sellers in the category:")
    #pprint(buyer.get_best_sellers())
