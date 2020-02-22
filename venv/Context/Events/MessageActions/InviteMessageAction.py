from Config import group_id, welcome_text
from Context.Events.BaseEvent import BaseEvent
from Context.Util.Vk.Message import Message

class InviteMessageAction(BaseEvent):
    def __init__(self, session, longpool):
        super(InviteMessageAction, self).__init__(session, longpool)

    def onEventReceive(self, event):
        is_bot_invited = event.object.message["action"]["member_id"] == -group_id
        if(is_bot_invited):
            peer_id = event.object.message['peer_id']
            Message(self._session).send(peer_id, welcome_text)