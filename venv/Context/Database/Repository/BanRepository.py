
from inject import attr;
from Context.Database.Database import Database;

class BanRepository(object):

    _db = attr(Database)

    def __init__(self, id, peer_id):
        self._id = id;
        self._peer_id = peer_id;

    def is_banned(self):
        response = self._db.fetchScalar("SELECT COUNT(*) FROM `block` WHERE `user_id` = %s and `peer_id` = %s",
                                        (self._id, self._peer_id))
        if int(response) > 0:
            return True
        return False

    def ban(self, reason):
        if self.is_banned() == False:
            self._db.sendNonReaderQuery("INSERT INTO `block`(`user_id`, `peer_id`, `reason`) VALUES (%s, %s, %s)",
                                        (self._id, self._peer_id, reason))

    def getBanDate(self):
        return self._db.fetchScalar("SELECT date FROM `block` WHERE `user_id` = %s and `peer_id` = %s",
                                        (self._id, self._peer_id))

    def getBanReason(self):
        return self._db.fetchScalar("SELECT reason FROM `block` WHERE `user_id` = %s and `peer_id` = %s",
                                        (self._id, self._peer_id))


    def unban(self):
        self._db.sendNonReaderQuery("DELETE FROM `block` WHERE `user_id` = %s and `peer_id` = %s ", (self._id, self._peer_id))

    def getGroupList(peer_id):
        return BanRepository._db.fetchResponse("SELECT user_id FROM `block` WHERE user_id < 0 and `peer_id` = %s LIMIT 50", (peer_id,))

    def getUserList(peer_id):
        return BanRepository._db.fetchResponse("SELECT user_id FROM `block` WHERE user_id > 0 and `peer_id` = %s LIMIT 50", (peer_id,))