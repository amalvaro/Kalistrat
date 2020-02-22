from Context.Events.BaseEvent import BaseEvent
from Context.Util.Map.Map import Map
from Context.Events.EventMaps.TextCommandsMap import TextCommandsMap
from Context.Database.Repository.UserRepository import UserRepository

class TextMessageAction(BaseEvent):
    def __init__(self, session, longpool):
        super(TextMessageAction, self).__init__(session, longpool)

    def isCommandGranted(self, event, commandOptions):

        sender_id = event.object.message['from_id']
        peer_id = event.object.message['peer_id']

        user = UserRepository(sender_id, peer_id)
        status = user.getUserStatus()

        if(status == None):
            status = 0

        if(status >= commandOptions["level"]):
            return True

        return False

    def executeTextCommand(self, text, event):
        args = text.split(' ')

        map = Map(args[0])
        equateBaseResult = map.equateBase(TextCommandsMap)

        eventCommandHandler = None;

        if(self.isCommandGranted(event, equateBaseResult.getArgs())):
            eventCommandHandler = equateBaseResult.getResult()

        if eventCommandHandler != None:
            eventHandler = eventCommandHandler(self._session, self._longpool, args)
            eventHandler.onEventReceive(event)

    def onEventReceive(self, event):

        text = event.object.message["text"].strip()
        if(text[0] == "/"):
            self.executeTextCommand(text, event)

