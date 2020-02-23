from Context.Util.Vk.Message import Message, MentionType
from Context.Events.BaseCommandEvent import BaseCommandEvent
from Config import group_id
from Context.Database.Repository.AdminRepository import AdminRepository

class KickCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(KickCommand, self).__init__(session, longpool, args)

    def kick(self, member_id, chat_id):
        Message(self._session).removeChatUser(chat_id, member_id)

    def onEventReceive(self, event):

        id = Message.getMention(event)

        if id != False:
            peer_id = event.object.message["peer_id"]
            member_id = id.getPeerId()

            self.kick(member_id, Message.getChatByPeer(peer_id))


