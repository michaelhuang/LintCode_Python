class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        i = m + n
        while m > 0 and n > 0:
            if A[m - 1] > B[n - 1]:
                A[i - 1] = A[m - 1]
                m -= 1
            else:
                A[i - 1] = B[n - 1]
                n -= 1
            i -= 1
        while n > 0:
            A[i - 1] = B[n - 1]
            n -= 1
            i -= 1
