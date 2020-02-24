from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Database.Repository.PeerRepository import PeerRepository
from Context.Util.Vk.Message import Message

class KickinviteCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(KickinviteCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]
        repos = PeerRepository(peer_id)
        repos.swtichCanInvite()

        if repos.canUserInvite() == False:
            Message(self._session).send(peer_id, "Теперь пользователи не могут приглашать других пользователей")
        else:
            Message(self._session).send(peer_id, "Теперь пользователи могут приглашать других пользователей")
