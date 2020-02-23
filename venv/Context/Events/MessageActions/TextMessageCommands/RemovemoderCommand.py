from Context.Events.BaseCommandEvent import BaseCommandEvent
from Config import AUTHORITY
from Context.Database.Repository.AdminRepository import AdminRepository
from Context.Util.Vk.Message import Message
from Context.Util.Vk.User import User

class RemovemoderCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(RemovemoderCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):

        peer_id = event.object.message["peer_id"]
        id = Message.getMention(event)

        if id != False:
            member_id = id.getPeerId()
            AdminRepository(member_id, peer_id).deleteAdmin()
            user_name = User(self._session).getUserName(member_id)
            Message(self._session).send(peer_id, "@id%s (%s) с вас сняты все права" % (member_id, user_name))