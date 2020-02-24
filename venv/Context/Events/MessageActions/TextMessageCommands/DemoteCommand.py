
import time
import threading
from Context.Events.BaseCommandEvent import BaseCommandEvent
from Context.Util.Vk.Message import Message
from Config import group_id
from Context.Database.Repository.AdminRepository import AdminRepository

class DemoteCommand(BaseCommandEvent):

    def __init__(self, session, longpool, args):
        super(DemoteCommand, self).__init__(session, longpool, args)

    def demote(self, message, peer_id, users):
        """
        :type message:Message
        :type users:list[object]
        :param message:Message
        :param users:array of users
        :return: void
        """

        for i in range(0, len(users)):
            user_id = users[i]["member_id"]
            try:
                if abs(int(user_id)) != group_id:
                    message.removeChatUser(Message.getChatByPeer(peer_id), user_id)
                    time.sleep(1)
            except:
                # handling whole people's that can not be excluded
                pass


    def onEventReceive(self, event):
        peer_id = event.object.message["peer_id"]
        from_id = event.object.message["from_id"]

        message = Message(self._session)
        users = message.getConversationMembers(peer_id)

        items = users["items"]

        if len(items) > 100:
            message.send(peer_id, "В беседе больше 100 человек")
            return


        t = threading.Thread(target=self.demote, args=(message, peer_id, items))
        t.start()