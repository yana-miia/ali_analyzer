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


class ProductSku(object):
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
        'property_identifiers': 'list[ProductPropertyVariationIdentifier]',
        'property_value_ids': 'list[int]',
        'product_id': 'str',
        'price': 'Amount',
        'stock': 'int',
        'image_url': 'str'
    }

    attribute_map = {
        'property_identifiers': 'propertyIdentifiers',
        'property_value_ids': 'propertyValueIds',
        'product_id': 'productId',
        'price': 'price',
        'stock': 'stock',
        'image_url': 'imageUrl'
    }

    def __init__(self, property_identifiers=None, property_value_ids=None, product_id=None, price=None, stock=None, image_url=None):  # noqa: E501
        """ProductSku - a model defined in OpenAPI"""  # noqa: E501

        self._property_identifiers = None
        self._property_value_ids = None
        self._product_id = None
        self._price = None
        self._stock = None
        self._image_url = None
        self.discriminator = None

        if property_identifiers is not None:
            self.property_identifiers = property_identifiers
        if property_value_ids is not None:
            self.property_value_ids = property_value_ids
        if product_id is not None:
            self.product_id = product_id
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock
        if image_url is not None:
            self.image_url = image_url

    @property
    def property_identifiers(self):
        """Gets the property_identifiers of this ProductSku.  # noqa: E501

        List of property variation identifiers   # noqa: E501

        :return: The property_identifiers of this ProductSku.  # noqa: E501
        :rtype: list[ProductPropertyVariationIdentifier]
        """
        return self._property_identifiers

    @property_identifiers.setter
    def property_identifiers(self, property_identifiers):
        """Sets the property_identifiers of this ProductSku.

        List of property variation identifiers   # noqa: E501

        :param property_identifiers: The property_identifiers of this ProductSku.  # noqa: E501
        :type: list[ProductPropertyVariationIdentifier]
        """

        self._property_identifiers = property_identifiers

    @property
    def property_value_ids(self):
        """Gets the property_value_ids of this ProductSku.  # noqa: E501

        List of property value IDs   # noqa: E501

        :return: The property_value_ids of this ProductSku.  # noqa: E501
        :rtype: list[int]
        """
        return self._property_value_ids

    @property_value_ids.setter
    def property_value_ids(self, property_value_ids):
        """Sets the property_value_ids of this ProductSku.

        List of property value IDs   # noqa: E501

        :param property_value_ids: The property_value_ids of this ProductSku.  # noqa: E501
        :type: list[int]
        """

        self._property_value_ids = property_value_ids

    @property
    def product_id(self):
        """Gets the product_id of this ProductSku.  # noqa: E501

        The ID of the product   # noqa: E501

        :return: The product_id of this ProductSku.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductSku.

        The ID of the product   # noqa: E501

        :param product_id: The product_id of this ProductSku.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def price(self):
        """Gets the price of this ProductSku.  # noqa: E501


        :return: The price of this ProductSku.  # noqa: E501
        :rtype: Amount
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ProductSku.


        :param price: The price of this ProductSku.  # noqa: E501
        :type: Amount
        """

        self._price = price

    @property
    def stock(self):
        """Gets the stock of this ProductSku.  # noqa: E501

        The stock of the product variation   # noqa: E501

        :return: The stock of this ProductSku.  # noqa: E501
        :rtype: int
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this ProductSku.

        The stock of the product variation   # noqa: E501

        :param stock: The stock of this ProductSku.  # noqa: E501
        :type: int
        """

        self._stock = stock

    @property
    def image_url(self):
        """Gets the image_url of this ProductSku.  # noqa: E501

        The image URL of the product variation   # noqa: E501

        :return: The image_url of this ProductSku.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ProductSku.

        The image URL of the product variation   # noqa: E501

        :param image_url: The image_url of this ProductSku.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

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
        if not isinstance(other, ProductSku):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
