
from inject import attr;
from Context.Database.Database import Database;

class AdminRepository(object):

    _db = attr(Database)

    def __init__(self, id, peer_id):
        self._id = id;
        self._peer_id = peer_id;

    def isCreated(self):

        response = self._db.fetchScalar("SELECT COUNT(*) FROM admins WHERE `user_id` = %s and `peer_id` = %s",
            (self._id, self._peer_id))

        if response != None:
            if response > 0:
                return True;

        return False

    def setAdminStatus(self, status):
        self._db.sendNonReaderQuery("UPDATE admins set user_status = %s WHERE `user_id` = %s and `peer_id` = %s ", (status, self._id, self._peer_id))

    def createAdmin(self, status):
        self._db.sendNonReaderQuery("INSERT INTO `admins`(`user_id`, `user_status`, `peer_id`) VALUES (%s,%s,%s)", (self._id, status, self._peer_id))

    def deleteAdmin(self):
        self._db.sendNonReaderQuery("DELETE FROM `admins` WHERE `user_id` = %s and `peer_id` = %s ", (self._id, self._peer_id))

    def getAdminStatus(self):
        response = self._db.fetchScalar("SELECT `user_status` FROM `admins` WHERE `user_id` = %s and `peer_id` = %s LIMIT 1", (self._id, self._peer_id))
        if response == None:
            return 0
        return response

    def getListByStatus(peer_id, status):
        return AdminRepository._db.fetchResponse("SELECT user_id FROM `admins` WHERE user_status=%s and `peer_id` = %s LIMIT 100", (status, peer_id))