
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

        if id != False:
            reason = ArgumentParser.combineArgsFrom(2, self.getCommandArgs())
            target_id = id.getPeerId()
            repos = WarnRepository(target_id, peer_id)

            message = Message(self._session)
            full_mention = message.getFullMention(id)
            repos.warn(reason)

            if (repos.is_warned() == False):
                message.send(peer_id, "%s получил(а) предупреждение с причиной %s" % (full_mention, reason))
            else:
                message.send(peer_id,
                             "%s был заблокирован (3/3) варнов с причиной %s" % (full_mention, reason))
                message.removeChatUser(Message.getChatByPeer(peer_id), target_id)
