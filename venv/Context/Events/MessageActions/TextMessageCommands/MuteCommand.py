from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Util.ArgumentParser.ArgumentParser import ArgumentParser
from Context.Util.Vk.Message import Message, MentionType
from Context.Database.Repository.MuteRepository import MuteRepository
from Context.Util.Vk.User import User

class MuteCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(MuteCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):

        peer_id = event.object.message["peer_id"]
        id = Message.getMention(event)

        if(id != False):
            reason = ArgumentParser.combineArgsFrom(2, self.getCommandArgs())

            if(id.getMentionType() == MentionType.USER):
                target_id = id.getPeerId()
                MuteRepository(target_id, peer_id).mute(reason)

                user_name = User(self._session).getUserName(target_id, "dat")
                Message(self._session).send(peer_id, "@id%s (%s) выдана блокировка чата с причиной %s" % (target_id,  user_name, reason))