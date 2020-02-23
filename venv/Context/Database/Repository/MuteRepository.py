
from inject import attr;
from Context.Database.Database import Database;

class MuteRepository(object):

    _db = attr(Database)

    def __init__(self, id, peer_id):
        self._id = id;
        self._peer_id = peer_id;

    def is_muted(self):
        response = self._db.fetchScalar("SELECT COUNT(*) FROM `mute` WHERE `user_id` = %s and `peer_id` = %s", (self._id, self._peer_id))
        if int(response) > 0:
            return True
        return False

    def mute(self, reason):
        if self.is_muted() == False:
            self._db.sendNonReaderQuery("INSERT INTO `mute`(`user_id`, `peer_id`, `reason`) VALUES (%s, %s, %s)", (self._id, self._peer_id, reason))
        else:
            self.updateReason(reason)

    def updateReason(self, reason):
        self._db.sendNonReaderQuery("UPDATE `mute` SET reason=%s WHERE `user_id` = %s and `peer_id` = %s ",
                                    (reason, self._id, self._peer_id))

    def unmute(self):
        self._db.sendNonReaderQuery("DELETE FROM `mute` WHERE `user_id` = %s and `peer_id` = %s ", (self._id, self._peer_id))

