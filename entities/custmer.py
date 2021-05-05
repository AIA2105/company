class Customer:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def getCustomer(self):
        customerData = 'ID',self.id,'Name',self.name,'Phone',self.phone
        return customerData
