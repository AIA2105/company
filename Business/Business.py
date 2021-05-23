from DataAccess import customerDB as S


class Business:

    # def AllCustomer():
    #     print('-----------------------------------------')
    #     cus=''
    #     customers = S.CustomerDB.FetchAll()
    #     for customer in customers:
    #         print(customer.getCustomer())
    #         cus=cus+customer.getCustomer()+'\n'
    #     print('-----------------------------------------')
    #     return cus

    def AllCustomersIds():
        ids = ''
        customers = S.CustomerDB.FetchAll()
        for customer in customers:
            ids=ids+customer.getId()+'\n'
        return ids

    def AllCustomersNames():
        names = ''
        customers = S.CustomerDB.FetchAll()
        for customer in customers:
            names=names+customer.getName()+'\n'
        return names

    def AllCustomersPhones():
        phones = ''
        customers = S.CustomerDB.FetchAll()
        for customer in customers:
            phones=phones+customer.getPhone()+'\n'
        return phones

    def CustomerID(id):
        print('-----------------------------------------')
        if int(id)-1<len(S.CustomerDB.FetchAll()):
            customers = S.CustomerDB.FetchAll()
            print(customers[int(id)-1].getCustomer())
            return customers[int(id)-1]
        else:
            print('Error in ID')
        print('-----------------------------------------')

    def CustomerName(name):
        print('-----------------------------------------')
        customers = S.CustomerDB.FetchByName(name)
        for c in customers:
            print(c.getCustomer())
            return c
        print('-----------------------------------------')
        # return customers

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
