from Context.Events.BaseEvent import BaseEvent

class InviteMessageAction(BaseEvent):
    def __init__(self, session, longpool):
        super(InviteMessageAction, self).__init__(session, longpool)

    def onEventReceive(self, event):

        print("User was invited")


        pass