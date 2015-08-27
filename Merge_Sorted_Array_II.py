class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        res, i, j = [], 0, 0
        while i < len(A) and j < len(B):
            if A[i] >= B[j]:
                res.append(B[j])
                j += 1
            else:
                res.append(A[i])
                i += 1
        if i < len(A):
            res.extend(A[i:])
        else:
            res.extend(B[j:])
        return res
