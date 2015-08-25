class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        if len(set(s) - set(t)) == 0:
            return True
        else:
            return False
