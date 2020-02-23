
import re

class ArgumentParser(object):

    def parseChatArguments(text):
        return re.findall("=?\[.*?\]|\S+", text)

    def combineArgsFrom(index, args):
        """
        :type index:integer
        :type args:list[string]
        :param index: combine from
        :param args: array of string
        :return: string

        """
        response = ""
        for i in range(index, len(args)):
            response = response + args[i] + " "

        return response.strip()