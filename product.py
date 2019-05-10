class Product:
    """
    Represent product.
    """


    def __init__(self, product_id='No Info', title='No Info',
                 category_id='No Info', price='No Info',
                 freight_price='No Info', currency='No Info', orders='No Info',
                 seller_name='No Info', seller_rating='No Info'):
        """
        Initialize product.
        """
        self.product_id = product_id
        self.title = title
        self.category_id = category_id
        self.price = price
        self.freight_price = freight_price
        self.currency = currency
        self.orders = orders
        self.seller_name = seller_name
        self.seller_rating = seller_rating

        if self.product_id == None:
            self.product_id = 'No Info'
        if self.title == None:
            self.title = 'No Info'
        if self.category_id == None:
            self.category_id = 'No Info'
        if self.price == None:
            self.price = 'No Info'
        if self.freight_price == None:
            self.freight_price = 'No Info'
        if self.currency == None:
            self.currency = 'No Info'
        if self.orders == None:
            self.orders = 'No Info'
        if self.seller_name == None:
            self.seller_name = 'No Info'
        if self.seller_rating == None:
            self.seller_rating = 'No Info'


    def __eq__(self, another):
        """
        Check if products are same.
        """
        return self.product_id == another.product_id


    def __ne__(self,another):
        """
        Check if products are different.
        """
        return not self == another


    def __str__(self):
        """
        Return data about product as a string.
        """
        return "Product id: " + str(self.product_id) + "\n" +\
                "Title: " + str(self.title) + "\n" +\
                "Category id: " + str(self.category_id) + "\n" +\
                "Price: " + str(self.price) + "\n" +\
                "Freight price: " + str(self.freight_price) + "\n" +\
                "Currency: " + str(self.currency) + "\n" +\
                "Orders: " + str(self.orders) + "\n" +\
                "Seller name: " + str(self.seller_name) + "\n" +\
                "Seller rating: " + str(self.seller_rating) + "\n"


class DetailedProduct(Product):
    """
    Represent extended information about the product.
    """


    def __init__(self, product_id='No Info', title='No Info',
                 category_id='No Info', price='No Info',
                 freight_price='No Info', currency='No Info', orders='No Info',
                 seller_name='No Info', seller_rating='No Info',
                 min_price='No Info', max_price='No Info',
                 wishlist='No Info'):

        super().__init__(product_id, title, category_id,
                         price, freight_price, currency, orders,
                         seller_name, seller_rating)

        self.min_price = min_price
        self.max_price = max_price
        self.wishlist = wishlist

        if self.product_id == None:
            self.product_id = 'No Info'
        if self.title == None:
            self.title = 'No Info'
        if self.category_id == None:
            self.category_id = 'No Info'
        if self.price == None:
            self.price = 'No Info'
        if self.freight_price == None:
            self.freight_price = 'No Info'
        if self.currency == None:
            self.currency = 'No Info'
        if self.orders == None:
            self.orders = 'No Info'
        if self.seller_name == None:
            self.seller_name = 'No Info'
        if self.seller_rating == None:
            self.seller_rating = 'No Info'
        if self.min_price == None:
            self.min_price = 'No Info'
        if self.max_price == None:
            self.max_price = 'No Info'
        if self.wishlist == None:
            self.wishlist = 'No Info'


    def __str__(self):
        return super().__str__() +\
               "Min price: " + str(self.min_price) + "\n" +\
               "Max price: " + str(self.max_price) + "\n" +\
               "Wish list count: " + str(self.wishlist) + "\n"
