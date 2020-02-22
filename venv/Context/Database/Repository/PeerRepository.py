
from inject import attr;
from Context.Database.Database import Database;

class PeerRepository(object):

    _db = attr(Database)

    def __init__(self, id, peer_id):
        self._id = id;
        self._peer_id = peer_id;

    def setAdminStatus(self, user_id, peer_id, status):
        self._db.sendNonReaderQuery("UPDATE admins set user_status = %s WHERE `user_id` = %s and `peer_id` = %s ", (status, user_id, peer_id))

    def createAdmin(self, user_id, peer_id):
        self._db.sendNonReaderQuery("INSERT INTO `admins`(`user_id`, `peer_id`) VALUES (%s,%s)", (user_id, peer_id))

    def deleteAdmin(self):
        self._db.sendNonReaderQuery("DELETE FROM `admins` WHERE `user_id` = %s and `peer_id` = %s ", (user_id, peer_id))

    def getAdminStatus(self):
        return self._db.fetchScalar("SELECT `user_status` FROM `admins` WHERE `user_id` = %s and `peer_id` = %s LIMIT 1", (self._id, self._peer_id))
