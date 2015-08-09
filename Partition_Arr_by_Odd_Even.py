class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        odds, evens = [], []
        for i in nums:
            evens.append(i) if i & 1 == 0 else odds.append(i)
        nums[:] = []  # empty the list
        nums.extend(odds)
        nums.extend(evens)


if __name__ == '__main__':
    a = Solution()
    a1 = [2147483644, 2147483645, 2147483646, 2147483647]
    a.partitionArray(a1)
    print a1
