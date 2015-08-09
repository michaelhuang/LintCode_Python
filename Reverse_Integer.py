class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        symbol = -1 if n < 0 else 1
        num = abs(n)
        res = symbol * int(str(num)[::-1])
        if -2147483648 <= res <= 2147483647:
            return res
        else:
            return 0
