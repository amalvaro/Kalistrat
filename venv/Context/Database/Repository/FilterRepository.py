
from inject import attr;
from Context.Database.Database import Database;

class FilterRepository(object):

    _db = attr(Database)

    def __init__(self, peer_id):
        self._peer_id = peer_id;

    def is_blocked(self, word):
        response = self._db.fetchScalar("SELECT COUNT(*) FROM `filter` WHERE `word` = %s and `peer_id` = %s", (word, self._peer_id))
        if int(response) > 0:
            return True
        return False

    def wordsAnalysis(self, words):
        """
        Word analysis
        :type words: list[string]
        :param words: Words list
        :return: boolean
        """

        count = len(words)
        if count > 1000:
            count = 1000

        queryPart = ""
        for i in range(0, count):
            queryPart = queryPart + ("\"%s\"," % (words[i]))

        if(queryPart != ""):
            queryPart = queryPart.strip()[0:-1]
            print("SELECT COUNT(*) FROM `filter` WHERE `word` in (%s) and `peer_id`=%s" % (queryPart, self._peer_id))
            response = self._db.fetchScalar("SELECT COUNT(*) FROM `filter` WHERE `word` in (%s) and `peer_id`=%s" % (queryPart, self._peer_id), None)
            #print(response)
            if response > 0:
                return True

        return False

    def add(self, word):
        if self.is_blocked(word) == False:
            self._db.sendNonReaderQuery("INSERT INTO `filter`(`word`, `peer_id`) VALUES (%s, %s)", (word, self._peer_id))

    def remove(self, word):
        self._db.sendNonReaderQuery("DELETE FROM `filter` WHERE `word` = %s and `peer_id`=%s", (word, self._peer_id))

    def getList(peer_id):
        return FilterRepository._db.fetchResponse("SELECT word FROM `filter` WHERE `peer_id`= %s LIMIT 500", (peer_id,))