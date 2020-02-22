
import abc

class BaseEvent(object):

    def __init__(self, session, longpool):
        self._session = session
        self._longpool = longpool

    @abc.abstractclassmethod
    def onEventReceive(self, event):
        pass
