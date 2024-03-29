
from Config import group_id
from Context.Util.Map.Map import Map
from vk_api.exceptions import ApiError
from Context.Events.BaseEvent import BaseEvent
from Context.Events.EventMaps.ApiErrorMap import ApiErrorMap
from Context.Events.EventMaps.EventListenerMap import EventListenerMap

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

        if eventClassHandler != None:
            eventHandler = eventClassHandler(self._session, self._longpool)
            try:
                eventHandler.onEventReceive(event)
            except ApiError as ae:
                mapError = Map(ae.code)
                eventApiErrorHandler = mapError.equate(ApiErrorMap)

                if(eventApiErrorHandler != None):
                    eventHandler = eventApiErrorHandler(self._session, self._longpool)
                    eventHandler.onEventReceive(event)
                else:
                    print(ae)