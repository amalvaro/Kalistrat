
from mysql.connector import connect

class Database(object):

    def __init__(self, host, database, user, password):
        self.__connection = connect(
            host=host,
            database=database,
            user=user,
            password=password
        )


    def sendNonReaderQuery(self, query):
        pass

    def fetchResponse(self, query):
        pass

    def fetchOnce(self, query):
        pass

    def fetchScalar(self, query):
        pass
