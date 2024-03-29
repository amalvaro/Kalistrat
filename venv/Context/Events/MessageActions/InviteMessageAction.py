from Config import group_id, welcome_text
from Context.Events.BaseEvent import BaseEvent
from Context.Util.Vk.Message import Message
from Context.Database.Repository.BanRepository import BanRepository
from Context.Database.Repository.WarnRepository import WarnRepository
from Context.Database.Repository.PeerRepository import PeerRepository
from Context.Database.Repository.AdminRepository import AdminRepository

class InviteMessageAction(BaseEvent):
    def __init__(self, session, longpool):
        super(InviteMessageAction, self).__init__(session, longpool)


    def is_banned(self, peer_id, user_id):
        if(BanRepository(user_id, peer_id).is_banned()):
            return True
        return False

    def is_warned(self, peer_id, user_id):
        if(WarnRepository(user_id, peer_id).is_warned()):
            return True
        return False

    def onEventReceive(self, event):
        from_id = event.object.message["from_id"]
        member_id = event.object.message["action"]["member_id"]
        is_bot_invited = member_id == -group_id

        message = Message(self._session)
        if(is_bot_invited):
            peer_id = event.object.message['peer_id']
            message.send(peer_id, welcome_text)
            repos = PeerRepository(peer_id)
            if repos.isCreated() == False:
                repos.create()

        peer_id = event.object.message["peer_id"]

        peer_repos = PeerRepository(peer_id)
        admin_repos = AdminRepository(from_id, peer_id)

        if peer_repos.canUserInvite() == False:
            if admin_repos.isCreated() == False:
                message.removeChatUser(Message.getChatByPeer(peer_id), member_id)


        if self.is_banned(peer_id, member_id) or self.is_warned(peer_id, member_id):
            message.removeChatUser(Message.getChatByPeer(peer_id), member_id)
            message.send(peer_id, "Пользователь заблокирован или заварнен")

