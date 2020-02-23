
from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Util.Vk.Message import Message
from Config import helpMessage

class HelpCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(HelpCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        Message(self._session).send(event.object.message["peer_id"], helpMessage)