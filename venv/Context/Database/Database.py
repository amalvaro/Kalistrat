
from mysql.connector import connect

class Database(object):

    def __init__(self, host, database, user, password):
        self.__connection = connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

    def getCursor(self, command, params = None):
        cursor = self.__connection.cursor()
        if(params != None):
            cursor.execute(command, params)
        else:
            cursor.execute(command)

        return cursor

    def sendNonReaderQuery(self, query, params):
        pass

    def fetchResponse(self, query, params):
        pass

    def fetchOnce(self, query, params):
        pass

    def fetchScalar(self, query, params):

        cursor = self.getCursor(query, params)
        data = cursor.fetchall()
        cursor.close()

        if len(data) == 1:
            return data[0][0]

        return None
