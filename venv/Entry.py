

from Config import token, group_id
from vk_api import VkApi
from inject import configure, attr

from Context.Database.Database import Database
from Context.VkGroupLongPool import VkGroupLongPool
from Context.Events.EventListener import EventListener
from Context.Database.DatabaseConfig import host, database, user, password


session = VkApi(token=token)
longpoll = VkGroupLongPool(session, group_id)


def dependencyConfiguration(binder):
    binder.bind(Database, Database(host, database, user, password))



configure(dependencyConfiguration);

event = EventListener(session, longpoll)
event.init()