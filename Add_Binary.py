class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        if len(a) < len(b): a, b = b, a
        pa = len(a) - 1
        pb = len(b) - 1
        carry = 0
        result = ''

        while pb >= 0:
            sum = int(a[pa]) + int(b[pb]) + carry
            result = str(sum%2) + result
            carry = sum / 2
            pb -= 1
            pa -= 1

        while pa >= 0:
            sum = int(a[pa]) + carry
            result = str(sum%2) + result
            carry = sum / 2
            pa -= 1

        if carry == 1: result = '1' + result
        return  result

if __name__ == '__main__':
    a = Solution()
    res = a.addBinary('110101','10010001011')
    print res