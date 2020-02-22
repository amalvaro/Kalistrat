from Context.Events.BaseEvent import BaseEvent

class InviteByLinkMessageAction(BaseEvent):
    def __init__(self, session, longpool):
        super(InviteByLinkMessageAction, self).__init__(session, longpool)

    def onEventReceive(self, event):

        print("User was invited by link")

        pass