from Context.Events.BaseCommandEvent import BaseCommandEvent

class KickCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(KickCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        print("Kick called")