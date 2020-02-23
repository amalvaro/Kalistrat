from Context.Events.BaseCommandEvent import BaseCommandEvent
from Config import AUTHORITY
from Context.Database.Repository.AdminRepository import AdminRepository
from Context.Util.Vk.Message import Message
from Context.Util.Vk.User import User


class ModerlistCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(ModerlistCommand, self).__init__(session, longpool, args)

    def defineSize(self, adminLists):
        adminListLen = 0
        nativeAdminListLen = adminLists

        if (nativeAdminListLen >= 500):
            adminListLen = 500
        else:
            adminListLen = nativeAdminListLen

        return adminListLen

    def onEventReceive(self, event):

        peer_id = event.object.message["peer_id"]
        adminLists = AdminRepository.getListByStatus(peer_id, AUTHORITY.MODERATOR)

        userIds = ""
        adminListLen = self.defineSize(len(adminLists))

        for i in range(0, adminListLen):
            userIds = userIds + str(adminLists[i][0]) + ","

        if(userIds != ""):
            users = User(self._session).getUserNames(userIds)

            messageString = ""
            for i in range(0, len(users)):
                messageString = messageString + "@id"+ str(users[i]["id"]) +" (" + users[i]["first_name"] + " " + users[i]["last_name"] + ")\n"

            if(messageString != ""):
                Message(self._session).send(peer_id, "Список модераторов: \n\n" + messageString)