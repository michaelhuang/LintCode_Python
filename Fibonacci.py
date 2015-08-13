class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        if n < 1: return None
        if n == 1: return 0
        if n == 2: return 1

        n_i, n_i_1, n_i_2 = 1, 1, 0
        for i in xrange(3, n):
            n_i_1, n_i_2 = n_i, n_i_1
            n_i = n_i_1 + n_i_2
        return n_i
