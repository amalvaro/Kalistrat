
from Context.Util.Map.Map import Map, BaseElement
from Context.Events.Exceptions.ChatAccessException import ChatAccessException

# The elements should be BaseEvent children.

ApiErrorMap = [
    BaseElement(ChatAccessException, 917)
    # ... and others
]