
class BaseElement(object):

    def __init__(self, result, standart, args = None):

        """
        :type args:dict
        :param args: List of args
        """

        self.__result = result
        self.__standart = standart
        self.__args = args

    def getResult(self):
        return self.__result;

    def getStandart(self):
        return self.__standart;

    def getArgs(self):
        return self.__args;

class Map(object):

    def __init__(self, trueStandart):
        self._trueStandart = trueStandart;

    def equateBase(self, map):
        """
        :type map:list[Element]
        :param map: map value, format: [{result: Object, standart: StandartEqualValue}, ..]
        :return: object

        """

        if map:
            for element in map:
                standart = element.getStandart()
                if standart == self._trueStandart:
                    return element;

        return None;

    def equate(self, map):

        response = self.equateBase(map)
        if(response != None):
            return response.getResult();

        return None