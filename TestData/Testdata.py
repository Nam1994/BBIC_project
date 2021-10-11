import json

from Objects.info_credit import Credit
from Objects.info_form import Info
from Utils.Utility import Utility


class TestData(object):
    BROWSER_NAME = "Chrome"
    BASE_URL = 'https://test.bbcincorp.com/make-payment'
    NAME = 'KHANH DO DANG'
    COMPANY = 'KMS COMPANY'
    NOTE = 'payment'
    EMAILS = 'khanhdo@gmail.com'
    AMOUNT = '500'
    CODE_VISA = '5555555555554444'
    DATE = '1221'
    CVC = '127'
    POSTAL = '70000'

    EXPECTED = 'Successful Payment'
    TEST_FILE = '../TestData/data.json'

    @staticmethod
    def get_form_data():
        info_form = Info(TestData.NAME, TestData.COMPANY, TestData.EMAILS, TestData.NOTE, TestData.AMOUNT)
        return info_form

    @staticmethod
    def get_credit_data():
        credit = Credit(TestData.CODE_VISA, TestData.DATE, TestData.CVC, TestData.POSTAL)
        return credit

    @staticmethod
    def form_info():
        with open(TestData.TEST_FILE) as file:
            data = json.load(file)

            form_info = data['form_info']
            name = form_info['name']
            company = form_info['company']
            email = form_info['email']
            note = form_info['note']
            amount = form_info['amount']

            form_information = Info(name, company, email, note, amount)
            return form_information

    @staticmethod
    def get_credit_info():
        with open(TestData.TEST_FILE) as file:
            data = json.load(file)

            credit_info = data['info_credit']
            numbers_card = credit_info['numbers_card']
            exp_date = credit_info['exp_date']
            cvc = credit_info['cvc']
            postal = credit_info['postal']

            credit_information = Credit(numbers_card, exp_date, cvc, postal)
            return credit_information

