import ctypes

class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        c = ctypes.c_uint32(a ^ b).value  # both a and b are 32-bit integers
        count = 0
        while c:
            c &= c - 1
            count += 1
        return count

if __name__ == '__main__':
    a = Solution()
    print a.bitSwapRequired(1, -1)
