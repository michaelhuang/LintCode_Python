class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        if s is None or len(s) == 0:
            return 0
        return len(s.split()[-1])
