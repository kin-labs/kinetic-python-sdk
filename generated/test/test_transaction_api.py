"""
    Kinetic

    The OpenAPI definition of the Kinetic API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.transaction_api import TransactionApi  # noqa: E501


class TestTransactionApi(unittest.TestCase):
    """TransactionApi unit test stubs"""

    def setUp(self):
        self.api = TransactionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_latest_blockhash(self):
        """Test case for get_latest_blockhash

          # noqa: E501
        """
        pass

    def test_get_minimum_rent_exemption_balance(self):
        """Test case for get_minimum_rent_exemption_balance

          # noqa: E501
        """
        pass

    def test_get_transaction(self):
        """Test case for get_transaction

          # noqa: E501
        """
        pass

    def test_make_transfer(self):
        """Test case for make_transfer

          # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
