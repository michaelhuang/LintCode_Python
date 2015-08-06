class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        carry = 1
        i = len(digits) - 1
        while i >= 0 and carry > 0:
            sum = digits[i] + carry
            digits[i] = sum % 10
            carry = sum / 10
            i -= 1

        if carry == 1:
            digits.insert(0, carry)
        return digits

if __name__ == '__main__':
    a1 = [1, 2, 3]
    a2 = [9, 9, 9]
    a = Solution()
    print a.plusOne(a1)
    print a.plusOne(a2)