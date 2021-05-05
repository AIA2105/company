from DataAccess import customerDB as S


class Business:

    def AllCustomer():
        print('-----------------------------------------')
        customers = S.CustomerDB.FetchAll()
        for customer in customers:
            print(customer.getCustomer())
        print('-----------------------------------------')

    def CustomerID(id):
        print('-----------------------------------------')
        if int(id)-1<len(S.CustomerDB.FetchAll()):
            customers = S.CustomerDB.FetchAll()
            print(customers[int(id)-1].getCustomer())
        else:
            print('Error in ID')
        print('-----------------------------------------')

    def CustomerName(name):
        print('-----------------------------------------')
        customers = S.CustomerDB.FetchByName(name)
        for c in customers:
            print(c.getCustomer())
        print('-----------------------------------------')

    def InsertCustomer(name,phone):
        print('-----------------------------------------')
        inserted = S.CustomerDB.InsertCustomer(name,phone)
        print(inserted)
        print('-----------------------------------------')

    def DeleteCustomer(id):
        print('-----------------------------------------')
        delete = S.CustomerDB.DeleteCustomer(id)
        print(delete)
        print('-----------------------------------------')

    def UpdateCustomerPhoneNumber(id, phone):
        print('-----------------------------------------')
        update = S.CustomerDB.UpdateCustomerPhoneNumber(id, phone)
        print(update)
        print('-----------------------------------------')
