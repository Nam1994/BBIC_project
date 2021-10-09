class Payment(object):

    def __init__(self, New_Incorporation, Banking_Service, Renewal_Fee, Legal_Ancillary_Service, Virtual_Office, Others):
        self.New_Incorporation = New_Incorporation
        self.Banking_Service = Banking_Service
        self.Renewal_Fee = Renewal_Fee
        self.Legal_Ancillary_Service = Legal_Ancillary_Service
        self.Virtual_Office = Virtual_Office
        self.Others = Others

    def __str__(self):
        return "New Incorporation is %s, Banking Service is %s, Renewal Fee is %s, Legal Ancillary Service is %s, " \
               "Virtual Office is %s, Others is %s " % (self.New_Incorporation, self.Banking_Service, self.Renewal_Fee,
                                                        self.Legal_Ancillary_Service, self.Virtual_Office, self.Others)
