from Context.Events.BaseEvent import BaseEvent
from Context.Util.Map.Map import Map
from Context.Events.EventMaps.TextCommandsMap import TextCommandsMap


class TextMessageAction(BaseEvent):
    def __init__(self, session, longpool):
        super(TextMessageAction, self).__init__(session, longpool)

    def onEventReceive(self, event):

        text = event.object.message["text"].strip()
        if(text[0] == "/"):
            args = text.split(' ');

            map = Map(args[0])
            eventCommandHandler = map.equate(TextCommandsMap)
            
            if eventCommandHandler != None:
                eventHandler = eventCommandHandler(self._session, self._longpool)
                eventHandler.onEventReceive(event)