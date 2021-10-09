from Locators.payment_locators import PaymentLocators
from Pages.base_page import BasePage
from TestData.Testdata import TestData
import logging
from Utils.assertion import Assertion


class PaymentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.navigate(TestData.BASE_URL)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def enter_info(self, info):
        self.enter_text(PaymentLocators.INPUT_YOUR_NAME, info.name)
        self.enter_text(PaymentLocators.INPUT_COMPANY, info.company)
        self.enter_text(PaymentLocators.INPUT_NOTE, info.note)
        self.enter_text(PaymentLocators.INPUT_Emails, info.email)
        self.enter_text(PaymentLocators.INPUT_AMOUNT, info.amount)

    def select_payment_info(self, payment):
        if payment.New_Incorporation:
            self.click(PaymentLocators.CHECKBOX_NEW_INC)
        if payment.Banking_Service:
            self.click(PaymentLocators.CHECKBOX_BANKING_SERVICE)
        if payment.Renewal_Fee:
            self.click(PaymentLocators.CHECKBOX_RENEWAL)
        if payment.Legal_Ancillary_Service:
            self.click(PaymentLocators.CHECKBOX_LEGAL_ANCILLARY_SERVICE)
        if payment.Virtual_Office:
            self.click(PaymentLocators.CHECKBOX_VIRTUAL_OFFICE)
        if payment.Others:
            self.click(PaymentLocators.CHECKBOX_OTHERS)

    def click_credit_card(self):
        credit = self.driver.find_element(*PaymentLocators.IMAGE_CREDIT_CARD)
        self.driver.execute_script("arguments[0].click();", credit)

    def click_payment_button(self):
        self.click(PaymentLocators.BUTTON_PAYMENT)

    def enter_credit_info(self, credit):
        iframe = self.get_element(PaymentLocators.LABEL_IFRAME_CREDIT)
        self.driver.switch_to.frame(iframe)
        self.enter_text(PaymentLocators.INPUT_CARD_NUMBERS, credit.numbers_card)
        self.enter_text(PaymentLocators.INPUT_EXP_DATE, credit.exp_date)
        self.enter_text(PaymentLocators.INPUT_CVC, credit.cvc)
        self.enter_text(PaymentLocators.INPUT_POSTAL, credit.postal)
        self.driver.switch_to.default_content()

    def click_pay_done(self):
        self.click(PaymentLocators.BUTTON_PAY)

    def actual_result(self):
        return self.get_text(PaymentLocators.LABEL_SUCCESSFULLY)

    def compare_results(self, actual_results, expected_results):
        Assertion().assertion(actual_results, expected_results, 'The result not match')

