import mysql.connector


class SQLConnector:

    def __init__(self, host, user, password, database):
        self.cnx = mysql.connector.connect(host=host, user=user,
                                           password=password, database=database)

    def connection(self):
        return self.cnx.cursor()
