class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x == 0:
            return 0
        guess = 1.0
        average = (x / guess + guess) / 2
        while abs(guess - average) >= 1:
            guess = average
            average = (x / guess + guess) / 2
        return int(guess)

