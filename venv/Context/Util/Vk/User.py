

class User(object):

    def __init__(self, session):
        self.__session = session

    def getUserNames(self, userId, name_case = ""):
        users = self.getUserById(userId, name_case)
        return users

    def getUserName(self, userId, name_case = ""):
        user = self.getUserById(userId, name_case)
        if(len(user) > 0):
            return user[0]["first_name"] + " " + user[0]["last_name"]
        else:
            return None

    def getUserIdByScreenName(self, screen_name):
        users = self.getUserById(screen_name)
        if (len(users) > 0):
            return users[0]["id"]
        else:
            return None

    def getUserById(self, userId, name_case = "", fields = ""):
        return self.__session.method('users.get', {'user_ids': userId, 'fields':fields, 'name_case':name_case, 'v': '5.103'})