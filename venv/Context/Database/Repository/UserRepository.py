
from inject import attr;
from Context.Database.Database import Database;

class UserRepository(object):

    _db = attr(Database)

    def __init__(self, id, chat_id):
        self._id = id;
        self._chat_id = chat_id;

    def wasRegistered(self):
        pass

    def createUser(self, userName, userPassword):
        pass

    def deleteUser(self):
        pass

