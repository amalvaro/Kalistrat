from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Database.Repository.FilterRepository import FilterRepository
from Context.Util.Vk.Message import Message

class FilterCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(FilterCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]
        args = self.getCommandArgs()
        repos = FilterRepository(peer_id)

        for i in range(1, len(args)):
            repos.add(args[i].strip().strip('\n').strip('\t'))

        Message(self._session).send(peer_id, "Было добавлено %d слово(в,а) в список" % (len(args) - 1))