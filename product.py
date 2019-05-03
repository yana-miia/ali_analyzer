class Product:
    """
    Represent product.
    """
    def __init__(self, title, category_id,
                 price, freight_price, currency,
                 seller_name, seller_rating):
        """
        Initialize product.
        """
        self.title = title
        self.category_id = category_id
        self.price = price
        self.freight_price = freight_price
        self.currency = currency
        self.seller_name = seller_name
        self.seller_rating = seller_rating

    def __str__(self):
        """
        Return data about product.
        """
        return "Title: " + self.title + "\n" +\
               "Category id: " + str(self.category_id) + "\n" +\
               "Price: " + str(self.price) + "\n" +\
               "Freight price: " + str(self.freight_price) + "\n" +\
               "Currency: " + self.currency + "\n" +\
               "Seller name: " + self.seller_name + "\n" +\
               "Seller rating: " + str(self.seller_rating) + "\n"
            
