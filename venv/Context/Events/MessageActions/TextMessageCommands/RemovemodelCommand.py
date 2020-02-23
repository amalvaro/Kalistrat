
from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Util.Vk.Message import Message
from Config import helpMessage

class HelpCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(HelpCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]
        Message(self._session).send(peer_id, helpMessage)