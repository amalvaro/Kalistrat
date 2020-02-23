
from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Database.Repository.WarnRepository import WarnRepository
from Context.Util.Vk.Message import Message, MentionType
from Context.Util.ArgumentParser.ArgumentParser import ArgumentParser
from Context.Util.Vk.User import User
from Context.Util.Vk.Group import Group

class WarnCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(WarnCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]

        id = Message.getMention(event)

        if(id != None):
            reason = ArgumentParser.combineArgsFrom(2, self.getCommandArgs())
            target_id = id.getId()
            repos = WarnRepository(target_id, peer_id)

            name    = ""
            prefix  = ""

            if (id.getMentionType() == MentionType.USER):
                name = User(self._session).getUserName(target_id, "dat")
                prefix = "id"
            else:
                name = Group(self._session).getGroupName(target_id)
                prefix = "club"

            message = Message(self._session)

            if (repos.is_warned() == False):
                repos.warn(reason)
                message.send(peer_id, "@%s%s (%s) выдано предупреждение с причиной %s" % (prefix, target_id, name, reason))
            else:
                message.send(peer_id,
                             "@%s%s (%s) был заблокирован (3/3) варнов с причиной %s" % (prefix, target_id, name, reason))
                message.removeChatUser(Message.getChatByPeer(peer_id), id.getPeerId())
