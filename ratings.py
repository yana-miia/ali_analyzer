class Ratings:
    """ Representation of the information about the seller's ratings.
        openapi_types (dict): The key is attribute name and the value is
        attribute type."""

    openapi_types = {
        'five_star_count': 'int',
        'four_star_count': 'int',
        'three_star_count': 'int',
        'two_star_count': 'int',
        'one_star_count': 'int',
        'total_count': 'int',
        'positive_count': 'int',
        'negative_count': 'int',
        'neutral_count': 'int',
        'ratings': 'float'
    }


    def __init__(self, five_star_count=None, four_star_count=None, \
                three_star_count=None, two_star_count=None, one_star_count=None,\
                total_count=None, positive_count=None, negative_count=None, \
                neutral_count=None, ratings=None):
        """
        Initialization.
        """
        self._five_star_count = None
        self._four_star_count = None
        self._three_star_count = None
        self._two_star_count = None
        self._one_star_count = None
        self._total_count = None
        self._positive_count = None
        self._negative_count = None
        self._neutral_count = None
        self._ratings = None

        if five_star_count is not None:
            self.five_star_count = five_star_count
        if four_star_count is not None:
            self.four_star_count = four_star_count
        if three_star_count is not None:
            self.three_star_count = three_star_count
        if two_star_count is not None:
            self.two_star_count = two_star_count
        if one_star_count is not None:
            self.one_star_count = one_star_count
        if total_count is not None:
            self.total_count = total_count
        if positive_count is not None:
            self.positive_count = positive_count
        if negative_count is not None:
            self.negative_count = negative_count
        if neutral_count is not None:
            self.neutral_count = neutral_count
        if ratings is not None:
            self.ratings = ratings


    def get_stars(self):
        """
        Function to get number of 1, 2, 3, 4, and 5 rating stars.
        Return the list of tuples, where the first element of the tuple is the
        star; the second element of the tuple is frequency of the star.
        """
        result = {'one star':self.one_star_count,
                  'two stars':self.two_star_count,
                  'three stars':self.three_star_count,
                  'four stars':self.four_star_count,
                  'five stars':self.five_star_count}
        return result


    def get_rating(self):
        """
        Get the rating according to the average value of all stars given.
        Renurn the float.
        """
        return self.get_ratings

    def get_positive_feedback_rate(self):
        """
        Get the pencent of positive feedbacks. Positive feedbacks are considered
        those which have 4-5 stars.
        Return the float.
        """
        result = (self.five_star_count + self.four_star_count)* 100/ self.total_count
        return round(result, 2)

    def get_negative_feedback_rate(self):
        """
        Get the pencent of negative feedbacks. Negative feedbacks are considered
        those which have 1-2 stars.
        Return the float.
        """
        result = (self.two_star_count + self.one_star_count)* 100/ self.total_count
        return round(result, 2)

    def get_neutral_feedback_rate(self):
        """
        Get the pencent of neutral feedbacks. Neutral feedbacks are considered
        those which have 3 stars.
        Return the float.
        """
        result = self.three_star_count * 100/ self.total_count
        return round(result, 2)

class SellerRatings(Ratings):
    """
    Representation of the ratings of seller.
    """

    def __init__(self):
        """
        Initialization.
        """

    # def get_shipping_speed(self):
    #     """
    #     Get the average speed of sending the product (do not confuse with delivery
    #     speed). The shipping speen is measured in numbers in range 1-5.
    #
    #     """
    #
    # def get_communication_level(self):
    #     """
    #     Get the average speed of answering to the customers. The communication
    #     level is measured in numbers in range 1-5.
    #     """
    #
    # def get_item_as_described_rate(self):
    #     """
    #     Get the average value in range 1-5 of the
    #     """


class BuyerRatings(Ratings):
    """
    Representation of the ratings of buyer.
    """

    def __init__(self):
        """
        Initialization.
        """
