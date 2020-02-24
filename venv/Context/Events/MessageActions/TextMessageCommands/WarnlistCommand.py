from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Database.Repository.WarnRepository import WarnRepository
from Context.Util.Vk.Message import Message

class WarnlistCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(WarnlistCommand, self).__init__(session, longpool, args)


    def onEventReceive(self, event):

        peer_id = event.object.message["peer_id"]

        groupList   = WarnRepository.getGroupList(peer_id)
        userList    = WarnRepository.getUserList(peer_id)

        messageOutput = "Список варнов: \n\n"

        for i in range(0, len(groupList)):
            messageOutput = messageOutput + "vk.com/public%s (%d/3) \n " % (abs(int(groupList[i][0])), groupList[i][1])

        for i in range(0, len(userList)):
            messageOutput = messageOutput + "vk.com/id%s (%d/3)\n" % (userList[i][0], userList[i][1])

        Message(self._session).send(peer_id, messageOutput)
