import time
from TestCases.base_test import BaseTest
from TestData.Testdata import TestData
from Objects.info_form import Info
from Pages.payment_page import PaymentPage
from Objects.info_credit import Credit
from Objects.payment import Payment
import unittest


class TestLoginPage(BaseTest):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_payment_page(self):
        payment_page = PaymentPage(self.driver)
        payment_page.enter_info(TestData.form_info())
        # payment_page.enter_info(TestData.get_form_data())
        payment = Payment(True, True, True, False, False, False)
        payment_page.select_payment_info(payment)
        payment_page.click_credit_card()
        payment_page.click_payment_button()
        # payment_page.enter_credit_info(TestData.get_credit_data())
        payment_page.enter_credit_info(TestData.get_credit_info())
        payment_page.click_pay_done()
        payment_page.compare_results(payment_page.actual_result(), TestData.EXPECTED)
        form_data = TestData.form_info()
        print(form_data.name)


if __name__ == "__main__":
    unittest.main()
