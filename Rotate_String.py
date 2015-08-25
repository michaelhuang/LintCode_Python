class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        if s is None or len(s) == 0:
            return None
        offset %= len(s)
        for j in xrange(offset):
            temp = s[-1]
            for i in xrange(len(s)-1, 0, -1):
                s[i] = s[i - 1]
            s[0] = temp


if __name__ == '__main__':
    a = Solution()
    s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    a.rotateString(s, 4)
    print s
