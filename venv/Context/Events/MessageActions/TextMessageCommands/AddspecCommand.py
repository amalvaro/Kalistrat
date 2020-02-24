from Context.Events.BaseCommandEvent import BaseCommandEvent
from Config import AUTHORITY
from Context.Database.Repository.AdminRepository import AdminRepository
from Context.Util.Vk.Message import Message
from Context.Util.Vk.User import User

class AddspecCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(AddspecCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]
        id = Message.getMention(event)
        if id != False:
            peer_id = event.object.message["peer_id"]
            member_id = id.getPeerId()
            repos = AdminRepository(member_id, peer_id)
            if repos.isCreated():
                repos.setAdminStatus(AUTHORITY.SPECIAL_ADMIN)
            else:
                repos.createAdmin(AUTHORITY.SPECIAL_ADMIN)
            user_name = User(self._session).getUserName(member_id)
            Message(self._session).send(peer_id, "@id%s (%s) вам выданы права главного администратора" % (member_id, user_name))