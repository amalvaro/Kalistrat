
import abc

class BaseEvent(object):

    def __init__(self, session, longpool):
        self._session = session
        self._longpool = longpool

    def onEventReceive(self, event):
        pass
