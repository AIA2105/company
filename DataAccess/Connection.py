# For Establish Connection

import mysql.connector as connection

class Connection:

    @staticmethod
    def get_connection():
        conn = connection.connect(host='localhost', user='ahmed', passwd='1234', database='company')
        if conn:
            return conn

    # @staticmethod
    # def create_connection():
    #     conn = Connection.get_connection()
    #     cur = conn.cursor()
    #     return cur

    # @staticmethod
    # def close_connection(connction, cursor):
    #     connction.commit()
    #     cursor.close()
    #     connction.close()
