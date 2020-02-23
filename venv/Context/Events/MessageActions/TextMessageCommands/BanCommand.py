from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Util.Vk.Message import Message, MentionType
from Context.Database.Repository.BanRepository import BanRepository
from Context.Util.Vk.Group import Group
from Context.Util.Vk.User import User
from Context.Util.ArgumentParser.ArgumentParser import ArgumentParser

class BanCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(BanCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):

        peer_id = event.object.message["peer_id"]
        id = Message.getMention(event)

        if (id != False):
            reason = ArgumentParser.combineArgsFrom(2, self.getCommandArgs())
            target_id = id.getPeerId()
            repos = BanRepository(target_id, peer_id)

            if(repos.is_banned() == False):
                repos.ban(reason)

            name = ""
            prefix = ""

            if(id.getMentionType() == MentionType.USER):
                name = User(self._session).getUserName(target_id, "dat")
                prefix="id"
            else:
                name = Group(self._session).getGroupName(id.getId())
                prefix="club"

            message = Message(self._session)
            message.send(peer_id, "@%s%s (%s) выдана блокировка с причиной %s" % (prefix, id.getId(), name, reason))
            message.removeChatUser(Message.getChatByPeer(peer_id), target_id)