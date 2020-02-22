
from Context.Util.Map.Map import Map, BaseElement
from Context.Events.MessageActions.InviteMessageAction import InviteMessageAction
from Context.Events.MessageActions.InviteByLinkMessageAction import InviteByLinkMessageAction

MessageEventMap = [
    BaseElement(InviteMessageAction, "chat_invite_user"),
    BaseElement(InviteByLinkMessageAction, "chat_invite_user_by_link"),
    # other's
]