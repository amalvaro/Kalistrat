from Config import group_id
from Context.Events.BaseEvent import BaseEvent

class InviteMessageAction(BaseEvent):
    def __init__(self, session, longpool):
        super(InviteMessageAction, self).__init__(session, longpool)

    def onEventReceive(self, event):

        is_bot_invited = event.object.message["action"]["member_id"] == -group_id
        if(is_bot_invited):
            # write message
            pass