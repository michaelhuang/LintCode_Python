class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        count = 0
        while num:
            count += 1
            num &= (num - 1)   # O(m) times for n bits with m 1 bits

        return count
