import re
from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Util.Vk.Message import Message
from Context.Util.Vk.User import User
from Context.Util.Vk.Group import Group
from Context.Util.Vk.Link import Link
from Context.Database.Repository.BanRepository import BanRepository
from Config import group_id

class UnbanCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(UnbanCommand, self).__init__(session, longpool, args)



    def onEventReceive(self, event):

        peer_id = event.object.message["peer_id"]
        args = self.getCommandArgs()
        pureIndex = Link.getPureIndex(args[len(args) - 1])

        if pureIndex == None:
            Message(self._session).send(peer_id, "Неверный идентификатор")
            return


        id = None
        if args[1] == "user":
            id = User(self._session).getUserIdByScreenName(pureIndex)
            BanRepository(id, peer_id).unban()
            Message(self._session).send(peer_id, "@id%s был разблокирован" % (id))

        elif args[1] == "group":
            id = Group(self._session).getGroupIdByScreenName(pureIndex)

            if(group_id != id):
                BanRepository(-id, peer_id).unban()
                Message(self._session).send(peer_id, "@public%s была разблокирована" % (id))

        else:
            Message(self._session).send(peer_id, "Укажите параметр: user / group")