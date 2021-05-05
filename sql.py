import mysql.connector as connection


db = connection.connect(host='localhost', user='ahmed', passwd='1234', database='company')
cr = db.cursor()
cr.execute('SELECT * FROM `customer`')
data = cr.fetchall()
print(data)


# cr.execute('INSERT INTO customer (name, phone) VALUES(%s, %s)',('Zeko Salama', '0123000000'))
#
# cr.execute('SELECT * FROM `customer`')
# data = cr.fetchall()
# print(data)

db.commit()
cr.close()
db.close()

