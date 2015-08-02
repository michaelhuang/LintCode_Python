class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        if len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            middle = (start + end) / 2
            if nums[middle] >= target:
                end = middle
            else:
                start = middle

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1

if __name__ == '__main__':
    a = Solution()

    a1 = [1, 2, 3, 3, 4, 5, 10]
    a2 = [1, 2, 3, 3, 3, 5]
    a3 = []
    a4 = [3]

    print a.binarySearch(a1, 3)
    print a.binarySearch(a2, 3)
    print a.binarySearch(a3, 3)
    print a.binarySearch(a4, 3)