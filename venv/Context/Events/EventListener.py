
from Config import group_id
from Context.Events.BaseEvent import BaseEvent
from Context.Events.EventMaps.EventListenerMap import EventListenerMap
from Context.Util.Map.Map import Map

class EventListener(BaseEvent):

    def __init__(self, session, longpool):
        super(EventListener, self).__init__(session, longpool)

    def init(self):

        for event in self._longpool.listen():
            self.onEventReceive(event)

    def onEventReceive(self, event):

        """
        Overrided BaseEvent method
        :type event:vk_api.bot_longpoll.VkBotMessageEvent
        :param event: Global VK Event
        """

        print(event)

        map = Map(event.type)
        eventClassHandler = map.equate(EventListenerMap)

        eventHandler = eventClassHandler(self._session, self._longpool)
        eventHandler.onEventReceive(event);