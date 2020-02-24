from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Database.Repository.FilterRepository import FilterRepository
from Context.Util.Vk.Message import Message

class FlistCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(FlistCommand, self).__init__(session, longpool, args)

    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]
        wordList = FilterRepository.getList(peer_id)

        messageOut = "Список заблокированных слов: \n"
        for i in range(0, len(wordList)):
            messageOut = messageOut + "%d. %s\n" % (i + 1, wordList[i][0])


        Message(self._session).send(peer_id, messageOut)