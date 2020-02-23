from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Database.Repository.BanRepository import BanRepository
from Context.Util.Vk.Message import Message
from Context.Util.Vk.Link import Link
from Context.Util.Vk.Group import Group
from Context.Util.Vk.User import User

class GetbanCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(GetbanCommand, self).__init__(session, longpool, args)


    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]

        args = self.getCommandArgs()
        message = Message(self._session)
        pureIndex = Link.getPureIndex(args[2])

        id = None
        if args[1] == "user":
            id = User(self._session).getUserIdByScreenName(pureIndex)

        elif args[1] == "group":
            id = Group(self._session).getGroupIdByScreenName(pureIndex)
            if id != None:
                id = -int(id)
        else:
            message.send(peer_id, "Укажите параметр: user / group")

        if id != None:

            respos = BanRepository(id, peer_id)
            date    = respos.getBanDate()
            reason  = respos.getBanReason()

            if date != None or reason != None:
                message.send(peer_id, "Пользователь заблокирован по причине %s %s" % (reason, date))
            else:
                message.send(peer_id, "Информация отсутствует")





        #if(id != None):
        #    pass



        # BanRepository()
