
class BaseElement(object):
    def __init__(self, result, standart):
        self.__result = result;
        self.__standart = standart;

    def getResult(self):
        return self.__result;

    def getStandart(self):
        return self.__standart;

class Map(object):

    def __init__(self, trueStandart):
        self._trueStandart = trueStandart;


    def equate(self, map):

        """
        :type map:list[Element]
        :param map: map value, format: [{result: Object, standart: StandartEqualValue}, ..]
        :return: object

        """

        if map:
            for element in map:
                standart = element.getStandart()
                if standart == self._trueStandart:
                    return element.getResult();

        return None;