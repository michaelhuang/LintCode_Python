class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        dict_A = {}
        for i in A:
            if i in dict_A:
                dict_A[i] += 1
            else:
                dict_A[i] = 1
        for i in B:
            if i in dict_A:
                dict_A[i] -= 1
                if dict_A[i] < 0:
                    return False
            else:
                return False
        return True
