from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Database.Repository.WarnRepository import WarnRepository
from Context.Util.Vk.Message import Message, MentionType
from Context.Util.ArgumentParser.ArgumentParser import ArgumentParser

class GetwarnCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(GetwarnCommand, self).__init__(session, longpool, args)

    def buildWarnsList(self, warnList):
        message = "Список варнов: \n"
        for i in range(0, len(warnList)):
            message = message + "%d. %s\n" % (i + 1, warnList[i][0])

        return message

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]
        id = Message.getMention(event)
        if id != False:

            message = Message(self._session)
            target_id = id.getPeerId()
            repos = WarnRepository(target_id, peer_id)

            if repos.has_warns() == False:
                message.send(peer_id, "У пользователя отсутствуют варны")
                return

            warnList = repos.getWarnList()
            messageOut = self.buildWarnsList(warnList)

            message.send(peer_id, messageOut)