
from inject import attr;
from Context.Database.Database import Database;

class WarnRepository(object):

    _db = attr(Database)

    def __init__(self, id, peer_id):
        self._id = id;
        self._peer_id = peer_id;

    def is_warned(self):
        response = self._db.fetchScalar("SELECT COUNT(*) FROM `warn` WHERE `user_id` = %s and `peer_id` = %s",
                                        (self._id, self._peer_id))
        if int(response) >= 2:
            return True
        return False

    def warn(self, reason):
        if self.is_warned() == False:
            self._db.sendNonReaderQuery("INSERT INTO `warn`(`user_id`, `peer_id`, `reason`) VALUES (%s, %s, %s)",
                                        (self._id, self._peer_id, reason))

    def unwarn(self, number):
        self._db.sendNonReaderQuery("DELETE FROM `warn` WHERE `user_id` = %s and `peer_id` = %s and `number`=%s LIMIT 1", (self._id, self._peer_id, number))

    def getGroupList(peer_id):
        return BanRepository._db.fetchResponse("SELECT user_id FROM `warn` WHERE user_id < 0 and `peer_id` = %s GROUP BY user_id LIMIT 50", (peer_id,))

    def getUserList(peer_id):
        return BanRepository._db.fetchResponse("SELECT user_id FROM `warn` WHERE user_id > 0 and `peer_id` = %s GROUP BY user_id  LIMIT 50", (peer_id,))