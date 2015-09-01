class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        majority, count = nums[0], 1
        for i in nums:
            if i == majority:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority = i
                    count = 1
        return majority
