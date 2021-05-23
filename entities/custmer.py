class Customer:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def getCustomer(self):
        customerData = ' ID: ',str(self.id),' ,Name: ',str(self.name),' ,Phone: ',str(self.phone)
        return ''.join(customerData)

    def getId(self):
        return str(self.id)

    def getName(self):
        return str(self.name)

    def getPhone(self):
        return str(self.phone)