

import re
from Context.Events.BaseEvent import BaseEvent
from Context.Util.Map.Map import Map
from Context.Events.EventMaps.TextCommandsMap import TextCommandsMap
from Context.Database.Repository.AdminRepository import AdminRepository
from Context.Util.ArgumentParser.ArgumentParser import ArgumentParser
from Context.Util.Vk.Message import Message, Mention, MentionType
from Context.Database.Repository.PeerRepository import PeerRepository

class ChatLeaveAction(BaseEvent):
    def __init__(self, session, longpool):
        super(ChatLeaveAction, self).__init__(session, longpool)

    def onEventReceive(self, event):

        peer_id = event.object.message["peer_id"]
        from_id = event.object.message["from_id"]

        member_id = event.object.message["action"]["member_id"]

        peer_repos = PeerRepository(peer_id)
        admin_repos = AdminRepository(from_id, peer_id)

        # it means that can user change a photo
        if peer_repos.isKickLeave() == False:
            if admin_repos.isCreated() == False:
                if member_id == from_id:
                    Message(self._session).removeChatUser(Message.getChatByPeer(peer_id), from_id)
