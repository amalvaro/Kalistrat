
from Context.Util.Map.Map import Map, BaseElement
from Context.Events.MessageActions.TextMessageCommands.KickCommand import KickCommand

TextCommandsMap = [
    BaseElement(KickCommand, "/kick", {"level": 0}),
    # other's
]