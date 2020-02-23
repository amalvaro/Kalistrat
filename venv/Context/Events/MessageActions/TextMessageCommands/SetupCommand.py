
from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Util.Vk.Message import Message
from Context.Util.Vk.User import User
from Context.Database.Repository.AdminRepository import AdminRepository
from Config import AUTHORITY

class SetupCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(SetupCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]
        from_id = event.object.message["from_id"]

        message = Message(self._session)
        members = message.getConversationMembers(peer_id)

        for member in members["items"]:
            if "is_owner" in member:
                if(member["is_owner"] == True and member["member_id"] == from_id):
                    self.giveFullAdministratorRights(from_id, peer_id)
                    name = User(self._session).getUserName(from_id, "dat")
                    message.send(peer_id, "Создателю беседы @id%s (%s) выданы полные права" % (from_id, name))
                    break

    def giveFullAdministratorRights(self, user_id, peer_id):

        repos = AdminRepository(user_id, peer_id)
        if(repos.isCreated()):
            repos.setAdminStatus(AUTHORITY.CREATOR_LEVEL)
        else:
            repos.createAdmin(AUTHORITY.CREATOR_LEVEL)