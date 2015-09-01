import sys

class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        min_sum, sum = sys.maxint, 0
        for i in nums:
            sum += i
            min_sum = min(min_sum, sum)
            sum = min(sum, 0)
        return min_sum
