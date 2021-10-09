class Info(object):

    def __init__(self, name, company, email, note, amount):
        self.name = name
        self.company = company
        self.email = email
        self.note = note
        self.amount = amount

    def __str__(self):
        return "Name is %s, Company is %s, Emails is %s, Note is %s, Amount is %s" % (self.name, self.company, self.email, self.note, self.amount)