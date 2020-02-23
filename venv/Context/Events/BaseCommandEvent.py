
import abc
from Context.Events.BaseEvent import BaseEvent

class BaseCommandEvent(BaseEvent):

    def __init__(self, session, longpool, args):
        super(BaseCommandEvent, self).__init__(session, longpool)
        self.__args = args

    def getCommandArgs(self):
        return self.__args;
