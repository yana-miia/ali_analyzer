# coding: utf-8

"""
    Aliseeks API

    AliExpress product searching and product details retrieval API.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SearchRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'text': 'str',
        'sort': 'str',
        'currency': 'NonRealtimeCurrency',
        'category': 'int',
        'include_subcategories': 'bool',
        'sort_direction': 'str',
        'ratings_range': 'DoubleRange',
        'quantity_range': 'IntegerRange',
        'price_range': 'DoubleRange',
        'unit_price_range': 'DoubleRange',
        'order_range': 'IntegerRange',
        'item_id_range': 'StringRange',
        'freight_types': 'list[str]',
        'skip': 'int',
        'limit': 'int',
        'scroll_pagination': 'bool',
        'scroll_identifier': 'str'
    }

    attribute_map = {
        'text': 'text',
        'sort': 'sort',
        'currency': 'currency',
        'category': 'category',
        'include_subcategories': 'includeSubcategories',
        'sort_direction': 'sortDirection',
        'ratings_range': 'ratingsRange',
        'quantity_range': 'quantityRange',
        'price_range': 'priceRange',
        'unit_price_range': 'unitPriceRange',
        'order_range': 'orderRange',
        'item_id_range': 'itemIdRange',
        'freight_types': 'freightTypes',
        'skip': 'skip',
        'limit': 'limit',
        'scroll_pagination': 'scrollPagination',
        'scroll_identifier': 'scrollIdentifier'
    }

    def __init__(self, text=None, sort='BEST_MATCH', currency=None, category=None, include_subcategories=False, sort_direction='ASC', ratings_range=None, quantity_range=None, price_range=None, unit_price_range=None, order_range=None, item_id_range=None, freight_types=None, skip=None, limit=None, scroll_pagination=False, scroll_identifier=None):  # noqa: E501
        """SearchRequest - a model defined in OpenAPI"""  # noqa: E501

        self._text = None
        self._sort = None
        self._currency = None
        self._category = None
        self._include_subcategories = None
        self._sort_direction = None
        self._ratings_range = None
        self._quantity_range = None
        self._price_range = None
        self._unit_price_range = None
        self._order_range = None
        self._item_id_range = None
        self._freight_types = None
        self._skip = None
        self._limit = None
        self._scroll_pagination = None
        self._scroll_identifier = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if sort is not None:
            self.sort = sort
        if currency is not None:
            self.currency = currency
        if category is not None:
            self.category = category
        if include_subcategories is not None:
            self.include_subcategories = include_subcategories
        if sort_direction is not None:
            self.sort_direction = sort_direction
        if ratings_range is not None:
            self.ratings_range = ratings_range
        if quantity_range is not None:
            self.quantity_range = quantity_range
        if price_range is not None:
            self.price_range = price_range
        if unit_price_range is not None:
            self.unit_price_range = unit_price_range
        if order_range is not None:
            self.order_range = order_range
        if item_id_range is not None:
            self.item_id_range = item_id_range
        if freight_types is not None:
            self.freight_types = freight_types
        if skip is not None:
            self.skip = skip
        if limit is not None:
            self.limit = limit
        if scroll_pagination is not None:
            self.scroll_pagination = scroll_pagination
        self.scroll_identifier = scroll_identifier

    @property
    def text(self):
        """Gets the text of this SearchRequest.  # noqa: E501

        The search query   # noqa: E501

        :return: The text of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SearchRequest.

        The search query   # noqa: E501

        :param text: The text of this SearchRequest.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def sort(self):
        """Gets the sort of this SearchRequest.  # noqa: E501


        :return: The sort of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this SearchRequest.


        :param sort: The sort of this SearchRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["PRODUCT_ID", "UPDATE_TIME", "WHOLESALE_PRICE", "ITEM_RATING", "ORDERS", "BEST_MATCH"]  # noqa: E501
        if sort not in allowed_values:
            raise ValueError(
                "Invalid value for `sort` ({0}), must be one of {1}"  # noqa: E501
                .format(sort, allowed_values)
            )

        self._sort = sort

    @property
    def currency(self):
        """Gets the currency of this SearchRequest.  # noqa: E501


        :return: The currency of this SearchRequest.  # noqa: E501
        :rtype: NonRealtimeCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SearchRequest.


        :param currency: The currency of this SearchRequest.  # noqa: E501
        :type: NonRealtimeCurrency
        """

        self._currency = currency

    @property
    def category(self):
        """Gets the category of this SearchRequest.  # noqa: E501

        The AliExpress category to search in   # noqa: E501

        :return: The category of this SearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SearchRequest.

        The AliExpress category to search in   # noqa: E501

        :param category: The category of this SearchRequest.  # noqa: E501
        :type: int
        """

        self._category = category

    @property
    def include_subcategories(self):
        """Gets the include_subcategories of this SearchRequest.  # noqa: E501

        When this flag is set to `true` the `category` field will be expanded so that all items in sub-categories will be included   # noqa: E501

        :return: The include_subcategories of this SearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_subcategories

    @include_subcategories.setter
    def include_subcategories(self, include_subcategories):
        """Sets the include_subcategories of this SearchRequest.

        When this flag is set to `true` the `category` field will be expanded so that all items in sub-categories will be included   # noqa: E501

        :param include_subcategories: The include_subcategories of this SearchRequest.  # noqa: E501
        :type: bool
        """

        self._include_subcategories = include_subcategories

    @property
    def sort_direction(self):
        """Gets the sort_direction of this SearchRequest.  # noqa: E501

        The direction to sort the results by. Only valid for certain `sort` values   # noqa: E501

        :return: The sort_direction of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction):
        """Sets the sort_direction of this SearchRequest.

        The direction to sort the results by. Only valid for certain `sort` values   # noqa: E501

        :param sort_direction: The sort_direction of this SearchRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASC", "DESC"]  # noqa: E501
        if sort_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_direction, allowed_values)
            )

        self._sort_direction = sort_direction

    @property
    def ratings_range(self):
        """Gets the ratings_range of this SearchRequest.  # noqa: E501


        :return: The ratings_range of this SearchRequest.  # noqa: E501
        :rtype: DoubleRange
        """
        return self._ratings_range

    @ratings_range.setter
    def ratings_range(self, ratings_range):
        """Sets the ratings_range of this SearchRequest.


        :param ratings_range: The ratings_range of this SearchRequest.  # noqa: E501
        :type: DoubleRange
        """

        self._ratings_range = ratings_range

    @property
    def quantity_range(self):
        """Gets the quantity_range of this SearchRequest.  # noqa: E501


        :return: The quantity_range of this SearchRequest.  # noqa: E501
        :rtype: IntegerRange
        """
        return self._quantity_range

    @quantity_range.setter
    def quantity_range(self, quantity_range):
        """Sets the quantity_range of this SearchRequest.


        :param quantity_range: The quantity_range of this SearchRequest.  # noqa: E501
        :type: IntegerRange
        """

        self._quantity_range = quantity_range

    @property
    def price_range(self):
        """Gets the price_range of this SearchRequest.  # noqa: E501


        :return: The price_range of this SearchRequest.  # noqa: E501
        :rtype: DoubleRange
        """
        return self._price_range

    @price_range.setter
    def price_range(self, price_range):
        """Sets the price_range of this SearchRequest.


        :param price_range: The price_range of this SearchRequest.  # noqa: E501
        :type: DoubleRange
        """

        self._price_range = price_range

    @property
    def unit_price_range(self):
        """Gets the unit_price_range of this SearchRequest.  # noqa: E501


        :return: The unit_price_range of this SearchRequest.  # noqa: E501
        :rtype: DoubleRange
        """
        return self._unit_price_range

    @unit_price_range.setter
    def unit_price_range(self, unit_price_range):
        """Sets the unit_price_range of this SearchRequest.


        :param unit_price_range: The unit_price_range of this SearchRequest.  # noqa: E501
        :type: DoubleRange
        """

        self._unit_price_range = unit_price_range

    @property
    def order_range(self):
        """Gets the order_range of this SearchRequest.  # noqa: E501


        :return: The order_range of this SearchRequest.  # noqa: E501
        :rtype: IntegerRange
        """
        return self._order_range

    @order_range.setter
    def order_range(self, order_range):
        """Sets the order_range of this SearchRequest.


        :param order_range: The order_range of this SearchRequest.  # noqa: E501
        :type: IntegerRange
        """

        self._order_range = order_range

    @property
    def item_id_range(self):
        """Gets the item_id_range of this SearchRequest.  # noqa: E501


        :return: The item_id_range of this SearchRequest.  # noqa: E501
        :rtype: StringRange
        """
        return self._item_id_range

    @item_id_range.setter
    def item_id_range(self, item_id_range):
        """Sets the item_id_range of this SearchRequest.


        :param item_id_range: The item_id_range of this SearchRequest.  # noqa: E501
        :type: StringRange
        """

        self._item_id_range = item_id_range

    @property
    def freight_types(self):
        """Gets the freight_types of this SearchRequest.  # noqa: E501

        Filter by freight types   # noqa: E501

        :return: The freight_types of this SearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._freight_types

    @freight_types.setter
    def freight_types(self, freight_types):
        """Sets the freight_types of this SearchRequest.

        Filter by freight types   # noqa: E501

        :param freight_types: The freight_types of this SearchRequest.  # noqa: E501
        :type: list[str]
        """

        self._freight_types = freight_types

    @property
    def skip(self):
        """Gets the skip of this SearchRequest.  # noqa: E501

        Skip a number of items, if you need to skip more than 10000 items then use the scroll feature   # noqa: E501

        :return: The skip of this SearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this SearchRequest.

        Skip a number of items, if you need to skip more than 10000 items then use the scroll feature   # noqa: E501

        :param skip: The skip of this SearchRequest.  # noqa: E501
        :type: int
        """
        if skip is not None and skip > 10000:  # noqa: E501
            raise ValueError("Invalid value for `skip`, must be a value less than or equal to `10000`")  # noqa: E501
        if skip is not None and skip < 0:  # noqa: E501
            raise ValueError("Invalid value for `skip`, must be a value greater than or equal to `0`")  # noqa: E501

        self._skip = skip

    @property
    def limit(self):
        """Gets the limit of this SearchRequest.  # noqa: E501

        Limit the request to a number of items   # noqa: E501

        :return: The limit of this SearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchRequest.

        Limit the request to a number of items   # noqa: E501

        :param limit: The limit of this SearchRequest.  # noqa: E501
        :type: int
        """
        if limit is not None and limit > 50:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `50`")  # noqa: E501
        if limit is not None and limit < 5:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `5`")  # noqa: E501

        self._limit = limit

    @property
    def scroll_pagination(self):
        """Gets the scroll_pagination of this SearchRequest.  # noqa: E501

        When this value is `true` then you will receive a scroll identifier which you can use to request the next page of results. The scroll identifier is good for 60 seconds.   # noqa: E501

        :return: The scroll_pagination of this SearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._scroll_pagination

    @scroll_pagination.setter
    def scroll_pagination(self, scroll_pagination):
        """Sets the scroll_pagination of this SearchRequest.

        When this value is `true` then you will receive a scroll identifier which you can use to request the next page of results. The scroll identifier is good for 60 seconds.   # noqa: E501

        :param scroll_pagination: The scroll_pagination of this SearchRequest.  # noqa: E501
        :type: bool
        """

        self._scroll_pagination = scroll_pagination

    @property
    def scroll_identifier(self):
        """Gets the scroll_identifier of this SearchRequest.  # noqa: E501

        The scroll identifier which can be retrieved by sending an initial search request with `scrollPagination` set to `true`. Scroll identifiers are good for 60 seconds.   # noqa: E501

        :return: The scroll_identifier of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._scroll_identifier

    @scroll_identifier.setter
    def scroll_identifier(self, scroll_identifier):
        """Sets the scroll_identifier of this SearchRequest.

        The scroll identifier which can be retrieved by sending an initial search request with `scrollPagination` set to `true`. Scroll identifiers are good for 60 seconds.   # noqa: E501

        :param scroll_identifier: The scroll_identifier of this SearchRequest.  # noqa: E501
        :type: str
        """

        self._scroll_identifier = scroll_identifier

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
