import re

class Link(object):

    def getPureIndex(rawIndex):

        match = re.search(r"(?:vk\.com[\/\\](?:id|public|club)(\d+))|(?:vk\.com[\/\\](\S+))", rawIndex)
        pureIndex = None
        if (match != None):

            groups_len = len(match.groups()) + 1
            for i in range(1, groups_len):
                group = match.group(i)
                if(group != None):
                    pureIndex = group
                    break
        else:
            pureIndex = rawIndex

        return pureIndex