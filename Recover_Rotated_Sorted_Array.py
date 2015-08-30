class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        left, right = 0, len(nums) - 1
        while left < right \
                and nums[left] >= nums[right]:
            mid = (left + right) / 2
            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] > nums[left]:
                left = mid + 1
            else:
                left += 1
        nums[:left] = nums[:left][::-1]
        nums[left:] = nums[left:][::-1]
        nums[:] = nums[:][::-1]

if __name__ == '__main__':
    a = Solution()
    nums = [4, 5, 1, 2, 3]
    a.recoverRotatedSortedArray(nums)
    print nums
