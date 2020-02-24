from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Database.Repository.PeerRepository import PeerRepository
from Context.Util.Vk.Message import Message

class KickphotoCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(KickphotoCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]
        repos = PeerRepository(peer_id)
        repos.swtichKickPhoto()

        if repos.isKickPhoto() == False:
            Message(self._session).send(peer_id, "Теперь пользователи будут исключены при смене фотографии беседы")
        else:
            Message(self._session).send(peer_id, "Теперь пользователи не будут исключены при смене фотографии беседы")
