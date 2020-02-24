from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Util.Vk.Message import Message

class KalistratCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(KalistratCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]
        Message(self._session).send(peer_id, "Я легко втираюсь в доверие. Я кот.")
