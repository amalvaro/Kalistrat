
from Context.Util.Map.Map import Map, BaseElement
from Context.Events.MessageActions.TextMessageCommands.KickCommand import KickCommand
from Context.Events.MessageActions.TextMessageCommands.SetupCommand import SetupCommand

TextCommandsMap = [
    BaseElement(KickCommand, "/kick", {"level": 1}),
    BaseElement(SetupCommand, "/setup", {"level": 0})
]