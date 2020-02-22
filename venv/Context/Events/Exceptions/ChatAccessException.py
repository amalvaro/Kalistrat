
from Context.Events.BaseEvent import BaseEvent
from Context.Util.Vk.Message import Message

class ChatAccessException(BaseEvent):

    def __init__(self, session, longpool):
        super(ChatAccessException, self).__init__(session, longpool)

    def onEventReceive(self, event):

        peer_id = event.object.message["peer_id"]
        Message(self._session).send(peer_id, "У меня нет доступа к данной функции (возможно отсутствуют права администратора). Выдайте права и введите /setup (выдача полномочий создателю беседы)")

        pass