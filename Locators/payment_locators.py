from selenium.webdriver.common.by import By


class PaymentLocators(object):
    '''Information form'''

    INPUT_YOUR_NAME = (By.NAME, 'your-name')
    INPUT_COMPANY = (By.NAME, 'your-order')
    INPUT_Emails = (By.NAME, 'your-email')
    INPUT_NOTE = (By.NAME, 'your-message')
    INPUT_AMOUNT = (By.NAME, 'amount')

    '''Payment for check box'''

    CHECKBOX_NEW_INC = (By.XPATH, "//input[@value='New Incorporation']")
    CHECKBOX_BANKING_SERVICE = (By.XPATH, "//input[@value='Banking Service']")
    CHECKBOX_RENEWAL = (By.XPATH, "//input[@value='Renewal Fee']")
    CHECKBOX_LEGAL_ANCILLARY_SERVICE = (By.XPATH, "//input[@value='Legal Ancillary Service']")
    CHECKBOX_VIRTUAL_OFFICE = (By.XPATH, "//input[@value='Virtual Office']")
    CHECKBOX_OTHERS = (By.XPATH, "//input[@value='Others']")

    IMAGE_CREDIT_CARD = (By.XPATH, "//div[@class='form-group payment-type']//input[@value='Card']")
    BUTTON_PAYMENT = (By.ID, 'make-payment-submit')

    '''Frame credit card'''

    LABEL_IFRAME_CREDIT = (By.XPATH, "//iframe[@title='Secure card payment input frame']")
    INPUT_CARD_NUMBERS = (By.XPATH, "//form[@class='ElementsApp is-empty']//input[@name='cardnumber']")
    INPUT_EXP_DATE = (By.XPATH, "//input[@name='exp-date']")
    INPUT_CVC = (By.XPATH, "//input[@name='cvc']")
    INPUT_POSTAL = (By.XPATH, "//input[@name='postal']")
    BUTTON_PAY = (By.ID, 'make-paymentStripe-submit')

    '''Results'''
    LABEL_SUCCESSFULLY = (By.XPATH, "//h1[text()='Successful Payment']")
