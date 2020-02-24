from Config import group_id, welcome_text
from Context.Events.BaseEvent import BaseEvent
from Context.Util.Vk.Message import Message
from Context.Database.Repository.BanRepository import BanRepository
from Context.Database.Repository.WarnRepository import WarnRepository

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
        member_id = event.object.message["action"]["member_id"]
        is_bot_invited = member_id == -group_id

        message = Message(self._session)
        if(is_bot_invited):
            peer_id = event.object.message['peer_id']
            message.send(peer_id, welcome_text)

        peer_id = event.object.message["peer_id"]

        if self.is_banned(peer_id, member_id) or self.is_warned(peer_id, member_id):
            message.removeChatUser(Message.getChatByPeer(peer_id), member_id)
            message.send(peer_id, "Пользователь заблокирован или заварнен")

