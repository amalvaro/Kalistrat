from Context.Events.BaseEvent import BaseEvent

class KickCommand(BaseEvent):

    def __init__(self, session, longpool):
        super(KickCommand, self).__init__(session, longpool)

    def onEventReceive(self, event):

        print("Kick called")




        pass