class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        if dictionary is None:
            return None

        res = []
        res.append(dictionary[0])
        for i in xrange(1, len(dictionary)):
            if len(res[0]) < len(dictionary[i]):
                res[:] = []
                res.append(dictionary[i])
            elif len(res[0]) == len(dictionary[i]):
                res.append(dictionary[i])
            else:
                None
        return res
