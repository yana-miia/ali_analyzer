class Product:
    """
    Represent product.
    """
    def __init__(self, title='No Info', category_id=0,
                 price=0, freight_price=0, currency='No Info', orders=0,
                 seller_name='No Info', seller_rating=0):
        """
        Initialize product.
        """
        self.title = title
        self.category_id = category_id
        self.price = price
        self.freight_price = freight_price
        self.currency = currency
        self.orders = orders
        self.seller_name = seller_name
        self.seller_rating = seller_rating
        if self.title == None:
            self.title = 'No Info'
        if self.category_id == None:
            self.category_id = 0
        if self.price == None:
            self.price = 0
        if self.freight_price == None:
            self.freight_price = 0
        if self.currency == None:
            self.currency = 'No Info'
        if self.orders == None:
            self.orders = 0
        if self.seller_name == None:
            self.seller_name = 'No Info'
        if self.seller_rating == None:
            self.seller_rating = 0

    def __eq__(self, another):
        """
        Check if equal.
        """
        if self.title == another.title and\
           self.category_id == another.category_id and\
           self.price == another.price and\
           self.fright_price == another.fright_price and\
           self.currency == another.currency and\
           self.orders == another.orders and\
           self.seller_name == another.seller_name and\
           self.seller_rating == another.seller_rating:
           return True
        else:
           return False

    def __ne__(self,another):
        """
        Check if not equal.
        """
        if self == another:
            return False
        else:
            return True

    def __str__(self):
        """
        Return data about product.
        """
        data = ""
        data += "Title: " + self.title + "\n" +\
                "Category id: " + str(self.category_id) + "\n" +\
                "Price: " + str(self.price) + "\n" +\
                "Freight price: " + str(self.freight_price) + "\n" +\
                "Currency: " + self.currency + "\n" +\
                "Orders: " + str(self.orders) + "\n" +\
                "Seller name: " + self.seller_name + "\n" +\
                "Seller rating: " + str(self.seller_rating) + "\n"
        return data
