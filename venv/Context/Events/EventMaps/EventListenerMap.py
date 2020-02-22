
from Context.Util.Map.Map import Map, BaseElement

from vk_api.bot_longpoll import VkBotEventType
from Context.Events.BaseEvent import BaseEvent
from Context.Events.MessageEvent import MessageEvent

# The elements should be BaseEvent children.

EventListenerMap = [
    BaseElement(MessageEvent, VkBotEventType.MESSAGE_NEW)
    # ... and others
]