from user import User
from ali_requests import search_products, get_product_info_by_id
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
        self.commands.update({"2 - demand": "Show you market demand with orders.",
                "3 - trend": "Return 'best products' in top category.",
                "4 - sellers": "Gives you list of best sellers with their rating.",
                "5 - statistic": "Show you statistic about product selling with " +\
                                    "their price, number of orders and profit.",
                "6 - recommendations": "Gives you expectations on each product."})


    def find_demand(self):
        """
        Find demand on each category in bestselling.
        Return list of tuples, where on 1st position are names of categories
        and on the 2nd - the quantities of orders in these categories.
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


    def get_trend(self):
        """
        Find trends of the market:
        The most popular categoty --> the most popular products.
        """
        top_category = self.find_demand()[0][0]
        return self.get_best_products(top_category) # added self.


    def get_best_sellers(self, category="All"):
        """
        Find Best Sellers in chosen category.
        It gives our seller the opportunity to compare himself with other
        sellers and get some knowledge from their experience on the market by
        exploring pages of their internet shops.
        """
        best_sellers = []
        for product in self.get_best_products(category):
            best_sellers.append({product.seller_name: product.seller_rating})
        return best_sellers


    def get_product_statistic(self, product_name):
        """
        Return dictionary with statistic about product selling, such as price of
        the product and number of times it had been ordered.
        """
        statistic = {}
        for product in search_products(product_name):
            statistic[product.seller_name] = \
                                {"price":product.price,
                                 "orders":product.orders,
                                 "profit":product.price * product.orders}
        return sorted(statistic.items(),
                      key=lambda x: x[1]["profit"],
                      reverse = True)


    def _filter_product(self, product_id):
        """
        Get usable information to predict product success.
        """
        product = get_product_info_by_id(product_id)
        product_data = {"title": product.title, "price": product.price,
                        "orders": product.orders, "wishlist": product.wishlist}
        return product_data


    def get_personal_recommendations(self, list_of_products):
        """
        Analyze product success in given range of products.
        """
        products = []
        for product_id in list_of_products:
            products.append(self._filter_product(product_id))
        products = sorted(products, key=lambda x: x["orders"], reverse = True)

        analyzed_products = []
        for product in products:
            predictable_orders = (round(product["orders"]\
                            /products[0]["orders"], 2) * product["wishlist"] +\
                            product["orders"]) // 1
            predictable_profit = predictable_orders * product["price"]
            analyzed_products.append({product["title"]:\
                                    {"predictable orders": predictable_orders,
                                    "predictable profit": predictable_profit}})

        return analyzed_products
