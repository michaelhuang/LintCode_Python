import sys
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        max_sum, sum = -sys.maxint - 1, 0
        for i in nums:
            sum += i
            max_sum = max(max_sum, sum)
            sum = max(sum, 0)
        return max_sum
