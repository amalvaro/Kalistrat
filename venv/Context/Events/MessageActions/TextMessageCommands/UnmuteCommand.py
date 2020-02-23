from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Util.ArgumentParser.ArgumentParser import ArgumentParser
from Context.Util.Vk.Message import Message, MentionType
from Context.Database.Repository.MuteRepository import MuteRepository
from Context.Util.Vk.User import User

class UnmuteCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(UnmuteCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):

        peer_id = event.object.message["peer_id"]
        id = Message.getMention(event)

        if(id != False):
            if(id.getMentionType() == MentionType.USER):
                target_id = id.getPeerId()
                MuteRepository(target_id, peer_id).unmute()

                user_name = User(self._session).getUserName(target_id, "dat")
                Message(self._session).send(peer_id, "@id%s (%s) снята блокировка чата" % (target_id,  user_name))