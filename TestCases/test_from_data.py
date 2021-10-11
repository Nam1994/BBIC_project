import time
from TestCases.base_test import BaseTest
from TestData.Testdata import TestData
import unittest


class TestLoginPage(BaseTest):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_product_page(self):
        dict = TestData.form_info()
        for i in dict:
            print(i)
        '''checkout = TestData.check_out_info()
        print(checkout)

        list = TestData.get_data()
        for i in list:
            print(i)

        overview = TestData.get_shipping_info()
        print(overview)'''


if __name__ == "__main__":
    unittest.main()
