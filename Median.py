class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        return self.__select(nums, (len(nums)-1)/2)

    def __select(self, nums, k):
        i = 0
        setlist = []
        while i + 5 < len(nums) - 1:       # why 5? see CLRS chapter 9.3
            setlist.append(nums[i : i+5])
            i += 5
        setlist.append(nums[i:])

        # Find the median of each of the n/5 groups
        medians = [sorted(sub)[(len(sub)-1)/2] for sub in setlist]
        # recursively to find the median x of the n/5 medians
        if len(medians) == 1:
            median = medians[0]
        else:
            median = self.__select(medians, (len(medians)-1) / 2)

        # Partition the input array around the median-of-medians x
        l1, l2, l3 = [], [], []
        for i in nums:
            if i < median:
                l1.append(i)
            elif i == median:
                l2.append(i)
            else:
                l3.append(i)

        if k < len(l1):
            return self.__select(l1, k)
        elif k < len(l1) + len(l2):
            return l2[0]
        else:
            return self.__select(l3, k - len(l1) - len(l2))

if __name__ == '__main__':
    a = Solution()
    # l1 = [4, 5, 1, 2, 3]
    # l2 = [7, 9, 4, 5]
    # l3 = [2, 2, 2, 3]
    # l4 = [2]
    # l5 = [1, 2, 3, 3, 3]
    l6 = [1,2,3,4,5,6,7,100,200,1000]

    # print a.median(l1)
    # print a.median(l2)
    # print a.median(l3)
    # print a.median(l4)
    # print a.median(l5)
    print a.median(l6)  # answer: 5


