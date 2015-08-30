class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        if len(A) == 0 or target <= A[0]: return 0
        if target == A[-1]: return len(A) - 1
        if target > A[-1]: return len(A)

        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if target <= A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
