
import re
import random
from enum import Enum

class MentionType(Enum):
    USER    = 0,
    CLUB    = 1

class Mention(object):
    def __init__(self, id, type):

        """
        :type id: integer
        :type: type: MentionType
        :param id: index
        :param type: type of index (group, user)
        """

        self._id = id
        self._type = type


        pass

    def getId(self):
        return self._id

    def getMentionType(self):
        return self._type

    def getPeerId(self):
        target = int(self._id)
        target = target if self.getMentionType() == MentionType.USER else -target
        return target

class Message(object):

    def __init__(self, session):
        self.__session = session

    def getConversationMembers(self, peer_id):
        return self.__session.method('messages.getConversationMembers', {'peer_id': peer_id, 'v': '5.103'})

    def send(self, peer_id, text):
        self.__session.method('messages.send', {'peer_id': peer_id,
                                                 'message': text,
                                                 'random_id': random.randint(0, 1000000000), 'v': '5.103'})

    def getMention(event):
        user_ids = Message.getMentions(event)

        if len(user_ids) != 0:
            return user_ids[0]
        else:
            return False

    def removeChatUser(self, chat_id, member_id):
        self.__session.method('messages.removeChatUser', {'chat_id': chat_id,
                                                'member_id': member_id, 'v': '5.103'})

    def getMentions(event):
        string = event.object.message["text"]
        user_ids = re.findall(r'\[(id|public|club)([- ]*\d*)\|.*\]', string)

        mentions = []
        for user in user_ids:

            type = None
            if(user[0] == "id"):
                type = MentionType.USER
            else:
                type = MentionType.CLUB

            mentions.append(Mention(int(user[1]), type))

        return mentions

    def getChatByPeer(peer_id):
        return  peer_id - 2000000000

    def getPeerByChat(chat_id):
        return chat_id + 2000000000