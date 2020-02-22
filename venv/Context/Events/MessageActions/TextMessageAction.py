from Context.Events.BaseEvent import BaseEvent

class TextMessageAction(BaseEvent):
    def __init__(self, session, longpool):
        super(TextMessageAction, self).__init__(session, longpool)

    def onEventReceive(self, event):

        print("Text was sended from user")


        pass