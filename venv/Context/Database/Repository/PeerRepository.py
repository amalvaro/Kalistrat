
from inject import attr;
from Context.Database.Database import Database;

class PeerRepository(object):

    _db = attr(Database)

    def __init__(self, peer_id):
        self._peer_id = peer_id;

    def create(self):
        self._db.sendNonReaderQuery("INSERT INTO `peer`(`peer_id`) VALUES (%s)", (self._peer_id,))

    def isCreated(self):
        response = self._db.fetchScalar("SELECT COUNT(*) FROM peer WHERE  `peer_id` = %s",
            (self._peer_id,))

        return self.getBooleanResponse(response)

    def getBooleanResponse(self, response):
        if response == None:
            return False

        if int(response) > 0:
            response = True
        else:
            response = False

        return response

    def isKickTitle(self):
        response = self._db.fetchScalar("SELECT kick_title FROM `peer` WHERE  `peer_id` = %s",
                                        (self._peer_id,))

        return self.getBooleanResponse(response)

    def isKickPin(self):
        response = self._db.fetchScalar("SELECT kick_pin FROM `peer` WHERE  `peer_id` = %s",
                                        (self._peer_id,))
        return self.getBooleanResponse(response)

    def isKickPhoto(self):
        response = self._db.fetchScalar("SELECT kick_photo FROM `peer` WHERE  `peer_id` = %s",
                                        (self._peer_id,))
        return self.getBooleanResponse(response)

    def isKickGroup(self):
        response = self._db.fetchScalar("SELECT kick_group FROM `peer` WHERE  `peer_id` = %s",
                                        (self._peer_id,))
        return self.getBooleanResponse(response)

    def isKickLeave(self):
        response = self._db.fetchScalar("SELECT kick_leave FROM `peer` WHERE  `peer_id` = %s",
                                        (self._peer_id,))
        return self.getBooleanResponse(response)

    def canUserInvite(self):
        response = self._db.fetchScalar("SELECT can_user_invite FROM `peer` WHERE  `peer_id` = %s",
                                        (self._peer_id,))
        return self.getBooleanResponse(response)

    def swtichKickGroup(self):
         self._db.sendNonReaderQuery("UPDATE `peer` SET `kick_group` = CASE WHEN `kick_group` = 1 THEN 0 WHEN `kick_group` = 0 THEN 1 END WHERE `peer_id`=%s", (self._peer_id,))


    def swtichKickTitle(self):
         self._db.sendNonReaderQuery("UPDATE `peer` SET `kick_title` = CASE WHEN `kick_title` = 1 THEN 0 WHEN `kick_title` = 0 THEN 1 END WHERE `peer_id`=%s", (self._peer_id,))


    def swtichKickPin(self):
         self._db.sendNonReaderQuery("UPDATE `peer` SET `kick_pin` = CASE WHEN `kick_pin` = 1 THEN 0 WHEN `kick_pin` = 0 THEN 1 END WHERE `peer_id`=%s", (self._peer_id,))


    def swtichKickPhoto(self):
         self._db.sendNonReaderQuery("UPDATE `peer` SET `kick_photo` = CASE WHEN `kick_photo` = 1 THEN 0 WHEN `kick_photo` = 0 THEN 1 END WHERE `peer_id`=%s", (self._peer_id,))


    def swtichKickLeave(self):
         self._db.sendNonReaderQuery("UPDATE `peer` SET `kick_leave` = CASE WHEN `kick_leave` = 1 THEN 0 WHEN `kick_leave` = 0 THEN 1 END WHERE `peer_id`=%s", (self._peer_id,))
         pass

    def swtichCanInvite(self):
         self._db.sendNonReaderQuery("UPDATE `peer` SET `can_user_invite` = CASE WHEN `can_user_invite` = 1 THEN 0 WHEN `can_user_invite` = 0 THEN 1 END WHERE `peer_id`=%s", (self._peer_id,))
         pass

