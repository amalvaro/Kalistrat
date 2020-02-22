
from time import sleep
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

class VkGroupLongPool(VkBotLongPoll):
    def listen(self):
        while (True):
            try:
                for event in self.check():
                    yield event
            except Exception as e:
                print(e)
            sleep(1)