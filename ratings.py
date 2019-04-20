class Ratings:
    """ Representation of the information about the seller's ratings."""
    def __init__(self):
        """
        Initialization.
        """

    def get_stars(self):
        """
        Function to get number of 1, 2, 3, 4, and 5 rating stars.
        Return the list of tuples, where the first element of the tuple is the
        star; the second element of the tuple is frequency of the star.
        """

    def get_rating(self):
        """
        Get the rating according to the average value of all stars given.
        Renurn the float.
        """

    def get_positive_feedback_rate(self):
        """
        Get the pencent of positive feedbacks. Positive feedbacks are considered
        those which have 4-5 stars.
        Return the float.
        """

    def get_negative_feedback_rate(self):
        """
        Get the pencent of negative feedbacks. Negative feedbacks are considered
        those which have 1-2 stars.
        Return the float.
        """

    def get_neutral_feedback_rate(self):
        """
        Get the pencent of neutral feedbacks. Neutral feedbacks are considered
        those which have 3 stars.
        Return the float.
        """

class SellerRatings(Ratings):
    """
    Representation of the ratings of seller.
    """

    def __init__(self):
        """
        Initialization.
        """

    def get_shipping_speed(self):
        """
        Get the average speed of sending the product (do not confuse with delivery
        speed). The shipping speen is measured in numbers in range 1-5.

        """

    def get_communication_level(self):
        """
        Get the average speed of answering to the customers. The communication
        level is measured in numbers in range 1-5.
        """

    def get_item_as_described_rate(self):
        """
        Get the average value in range 1-5 of the
        """


class BuyerRatings(Ratings):
    """
    Representation of the ratings of buyer.
    """

    def __init__(self):
        """
        Initialization.
        """
