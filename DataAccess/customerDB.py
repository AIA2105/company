# For SQL Commands and methods on Student
import mysql

from DataAccess import Connection as C
from entities import custmer as S

class CustomerDB:

    def FetchAll():
        List_Of_Customers = []
        conn = C.Connection.get_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM `customer`')
        List_Of_Tuples = cur.fetchall()

        for tuple in List_Of_Tuples:
            List_Of_Customers.append(S.Customer(tuple[0],tuple[1],tuple[2]))

        return List_Of_Customers

    def FetchByName(name):
        List_Of_Customers = []
        conn = C.Connection.get_connection()
        cur=conn.cursor()
        cur.execute('SELECT * FROM customer WHERE name= %s',(name,))
        List_Of_Tuples = cur.fetchall()

        for tuple in List_Of_Tuples:
            List_Of_Customers.append(S.Customer(tuple[0],tuple[1],tuple[2]))

        return List_Of_Customers

    def InsertCustomer(name,phone):
        conn = C.Connection.get_connection()
        cur=conn.cursor()
        cur.execute('INSERT INTO customer (name, phone) VALUES(%s, %s)',(name, phone))
        conn.commit()
        cur.close()
        conn.close()
        return 'Inserted'

    def DeleteCustomer(id):
        conn = C.Connection.get_connection()
        cur=conn.cursor()
        cur.execute('DELETE FROM `company`.`customer` WHERE `id`= %s',(id,))
        conn.commit()
        cur.close()
        conn.close()
        return 'Deleted'

    def UpdateCustomerPhoneNumber(id,phone):
        conn = C.Connection.get_connection()
        cur=conn.cursor()
        cur.execute('UPDATE `company`.`customer` SET `phone`=%s WHERE `id`= %s',(phone,id,))
        conn.commit()
        cur.close()
        conn.close()
        return 'Updated'


