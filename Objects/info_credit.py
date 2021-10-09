class Credit(object):

    def __init__(self, numbers_card, exp_date, cvc, postal):
        self.numbers_card = numbers_card
        self.exp_date = exp_date
        self.cvc = cvc
        self.postal = postal

    def __str__(self):
        return "Numbers is %s, Exp date is %s, CVC is %s, Postal is %s" % (self.numbers_card, self.exp_date, self.cvc, self.postal)