from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Database.Repository.BanRepository import BanRepository
from Context.Util.Vk.Message import Message

class BanlistCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(BanlistCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]

        groupList   = BanRepository.getGroupList(peer_id)
        userList    = BanRepository.getUserList(peer_id)

        messageOutput = "Список заблокированных: \n\n"

        for i in range(0, len(groupList)):
            messageOutput = messageOutput + "vk.com/public%s\n" % (abs(int(groupList[i][0])))

        for i in range(0, len(userList)):
            messageOutput = messageOutput + "vk.com/id%s\n" % (userList[i][0])

        Message(self._session).send(peer_id, messageOutput)