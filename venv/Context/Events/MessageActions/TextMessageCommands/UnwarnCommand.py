
from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Database.Repository.WarnRepository import WarnRepository
from Context.Util.Vk.Message import Message, MentionType, Mention
from Context.Util.ArgumentParser.ArgumentParser import ArgumentParser
from Context.Util.Vk.User import User
from Context.Util.Vk.Group import Group
from Context.Util.Vk.Link import Link
from Config import group_id

class UnwarnCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(UnwarnCommand, self).__init__(session, longpool, args)

    def defineId(self,  mention, args):
        object_index = None

        if mention != False:
            object_index = mention.getPeerId()
        else:
            pureIndex = Link.getPureIndex(args[len(args) - 1])
            if pureIndex != None:
                if args[1] == "user":
                    object_index = User(self._session).getUserIdByScreenName(pureIndex)
                    if(object_index != None):
                        object_index = int(object_index)
                elif args[1] == "group":
                    index = Group(self._session).getGroupIdByScreenName(pureIndex)
                    if index != None:
                        object_index = -int(index)
                else:
                    # it means that a required argument was not found
                    return False

        return object_index

    def onEventReceive(self, event):

        peer_id = event.object.message["peer_id"]
        object_index = self.defineId(Message.getMention(event), self.getCommandArgs())

        if object_index != None:

            if object_index == False:
                Message(self._session).send(peer_id,
                                            "В случае, когда указана ссылка введите /unwarn [group/user] [link]")
                return

            message = Message(self._session)
            if(abs(object_index) == group_id):
                return

            repos = WarnRepository(object_index, peer_id)
            if(repos.has_warns()) == False:
                message.send(peer_id, "У пользователя нет варнов")
                return

            repos.unwarn()

            type = MentionType.CLUB
            if object_index > 0:
                type = MentionType.USER

            mention = Mention(abs(object_index), type)
            full_mention = message.getFullMention(mention)

            message.send(peer_id, "С %s было снято одно предупреждение" % (full_mention))