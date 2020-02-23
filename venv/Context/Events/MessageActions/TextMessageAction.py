

from Context.Events.BaseEvent import BaseEvent
from Context.Util.Map.Map import Map
from Context.Events.EventMaps.TextCommandsMap import TextCommandsMap
from Context.Database.Repository.AdminRepository import AdminRepository
from Context.Database.Repository.MuteRepository import MuteRepository
from Context.Util.ArgumentParser.ArgumentParser import ArgumentParser
from Context.Util.Vk.Message import Message
from Config import errorAuthorityCommandExecution, group_id

class TextMessageAction(BaseEvent):
    def __init__(self, session, longpool):
        super(TextMessageAction, self).__init__(session, longpool)

    def isCommandGranted(self, event, commandOptions):

        sender_id = event.object.message['from_id']
        peer_id = event.object.message['peer_id']

        user = AdminRepository(sender_id, peer_id)
        status = user.getAdminStatus()

        if(status == None):
            status = 0

        target = Message.getMention(event)
        if(target != False):
            target_status = AdminRepository(target.getPeerId(), peer_id).getAdminStatus()
            if(target_status >= status or target.getId() == group_id):
                Message(self._session).send(peer_id, errorAuthorityCommandExecution)
                return False

        if(status >= commandOptions["level"]):
            return True

        return False

    def checkArgsCount(self, currentCount, commandOptionsCount):
        if currentCount >= commandOptionsCount:
            return True
        else:
            return False

    def executeTextCommand(self, text, event):

        args = ArgumentParser.parseChatArguments(text)

        if(len(args) == 0):
            return

        map = Map(args[0])
        equateBaseResult = map.equateBase(TextCommandsMap)

        if(equateBaseResult == None):
            return

        eventCommandHandler = None;

        commandOptions = equateBaseResult.getArgs()
        if(equateBaseResult != None):
            if(self.isCommandGranted(event, commandOptions)):
                eventCommandHandler = equateBaseResult.getResult()

        if self.checkArgsCount(len(args), commandOptions["count_args"]) == False:
            Message(self._session).send(event.object.message["peer_id"], commandOptions["args_exc"])
            return

        if eventCommandHandler != None:
            eventHandler = eventCommandHandler(self._session, self._longpool, args)
            eventHandler.onEventReceive(event)

    def isMuted(self, user_id, peer_id):
        return MuteRepository(user_id, peer_id).is_muted()

    def onEventReceive(self, event):

        text = event.object.message["text"].strip()
        if(text[0] == "/"):
            self.executeTextCommand(text, event)

        peer_id = event.object.message["peer_id"]
        from_id = event.object.message["from_id"]

        if self.isMuted(from_id, peer_id):
            message = Message(self._session)
            message.removeChatUser(Message.getChatByPeer(peer_id), from_id)
            message.send(peer_id, "У пользователя @id%s блокировка чата" % (from_id))