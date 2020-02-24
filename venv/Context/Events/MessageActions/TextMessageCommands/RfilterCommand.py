from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Database.Repository.FilterRepository import FilterRepository
from Context.Util.Vk.Message import Message

class RfilterCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(RfilterCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]
        args = self.getCommandArgs()
        repos = FilterRepository(peer_id)

        for i in range(1, len(args)):
            repos.remove(args[i])

        Message(self._session).send(peer_id, "Было удалено %d слово(в,а) из списка" % (len(args) - 1))