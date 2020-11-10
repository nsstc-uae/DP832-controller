import mysql.connector
from mysql.connector import Error
class connection:
    cursor=None
    connection=None
    def connect(self,current, channel, voltage):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                database='psuDB',
                                                user='root',
                                                password='password11')
            if self.connection.is_connected():
                dp_Info= self.connection.get_server_info()
                print("Connection to MySQL server version ", dp_Info)
                self.cursor=self.connection.cursor()
                self.cursor.execute("use psuDB;")
                self.connection.commit()
                mySqlQuery = (
                    "INSERT INTO results (Channel, Time, Current, Voltage) "
                    "VALUES ("+channel+" , NOW(), "+current+", "+voltage+");")
                #data = (channel, current, voltage)
                self.cursor.execute(mySqlQuery)
                self.connection.commit()


        except Error as e:
            print("Error while connecting ", e)

        finally:
            if (self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
                print("MySQL connection is closed")

    def sendToDB(self, current, channel):
        try:
            mySqlQuery = (
                "INSERT INTO result (Current, Time, Channel) "
                "VALUES (%s, NOW(), %s);")
            data = (str(current),  str(channel))
            #print(mySqlQuery)
            #print(data)

            self.cursor.execute(mySqlQuery,data)
            self.connection.commit()
        except Error as e:
            print("Error at query: ", e)

    def closeConnection(self):
        try:
            #if self.connection.is_connected():
            self.cursor.colse()
            self.connection.commit()
            self.connection.close()
            print("connection closed")
        except Error as e:
            print("Error when closing connection: ", e)
