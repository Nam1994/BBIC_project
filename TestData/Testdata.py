from Objects.info_credit import Credit
from Objects.info_form import Info


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

    @staticmethod
    def get_form_data():
        info_form = Info(TestData.NAME, TestData.COMPANY, TestData.EMAILS, TestData.NOTE, TestData.AMOUNT)
        return info_form

    @staticmethod
    def get_credit_data():
        credit = Credit(TestData.CODE_VISA, TestData.DATE, TestData.CVC, TestData.POSTAL)
        return credit