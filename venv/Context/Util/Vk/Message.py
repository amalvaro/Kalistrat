
import random

class Message(object):

    def __init__(self, session):
        self.__session = session

    def getConversationMembers(self, peer_id):
        return self.__session.method('messages.getConversationMembers', {'peer_id': peer_id, 'v': '5.103'})

    def send(self, peer_id, text):
        self.__session.method('messages.send', {'peer_id': peer_id,
                                                 'message': text,
                                                 'random_id': random.randint(0, 1000000000), 'v': '5.103'})