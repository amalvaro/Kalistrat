

class Group(object):

    def __init__(self, session):
        self.__session = session

    def getGroupNames(self, userId):
        groups = self.getGroupName(userId)
        return groups

    def getGroupName(self, groupId):
        groups = self.getGroupById(groupId)
        if(len(groups) > 0):
            return groups[0]["name"]
        else:
            return None

    def getGroupIdByScreenName(self, screen_name):
        groups = self.getGroupById(screen_name)
        if (len(groups) > 0):
            return int(groups[0]["id"])
        else:
            return None

    def getGroupById(self, groupIds):
        return self.__session.method('groups.getById', {'group_ids': groupIds, 'v': '5.103'})