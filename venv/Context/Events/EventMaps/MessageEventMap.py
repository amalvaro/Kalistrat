
from Context.Util.Map.Map import Map, BaseElement
from Context.Events.MessageActions.InviteMessageAction import InviteMessageAction
from Context.Events.MessageActions.InviteByLinkMessageAction import InviteByLinkMessageAction
from Context.Events.MessageActions.ChatTitleUpdateAction import ChatTitleUpdateAction
from Context.Events.MessageActions.ChatUnpinAction import ChatUnpinAction
from Context.Events.MessageActions.ChatPhotoChangeAction import ChatPhotoChangeAction
from Context.Events.MessageActions.ChatLeaveAction import ChatLeaveAction

MessageEventMap = [
    BaseElement(InviteMessageAction, "chat_invite_user"),
    BaseElement(InviteByLinkMessageAction, "chat_invite_user_by_link"),
    BaseElement(ChatTitleUpdateAction, "chat_title_update"),
    BaseElement(ChatUnpinAction, "chat_unpin_message"),
    BaseElement(ChatPhotoChangeAction, "chat_photo_update"),
    BaseElement(ChatPhotoChangeAction, "chat_photo_remove"),
    BaseElement(ChatLeaveAction, "chat_kick_user")
    # other's
]