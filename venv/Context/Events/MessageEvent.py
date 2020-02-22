
from Context.Util.Map.Map import Map
from Context.Events.BaseEvent import BaseEvent
from Context.Events.EventMaps.MessageEventMap import MessageEventMap
from Context.Events.MessageActions.TextMessageAction import TextMessageAction

class MessageEvent(BaseEvent):
    def __init__(self, session, longpool):
        super(MessageEvent, self).__init__(session, longpool)

    def onEventReceive(self, event):

        """
        Overrided BaseEvent method
        :type event:vk_api.bot_longpoll.VkBotMessageEvent
        :param event: Global VK Event
        """


        eventHandler = None

        if("action" in event.object.message):
            map = Map(event.object.message["action"]["type"])
            eventActionHandler = map.equate(MessageEventMap)

            if eventActionHandler != None:
                eventHandler = eventActionHandler(self._session, self._longpool)


        else:
            eventHandler = TextMessageAction(self._session, self._longpool)

        if eventHandler != None:
            eventHandler.onEventReceive(event);