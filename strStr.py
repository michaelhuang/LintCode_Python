class Solution:
    def strStr(self, source, target):
        if source is not None and target is not None:
            for i in xrange(len(source) - len(target) + 1):
                j = 0
                while j < len(target):
                    if source[i+j] != target[j]:
                        break
                    j += 1
                if j == len(target):
                    return i
        return -1
