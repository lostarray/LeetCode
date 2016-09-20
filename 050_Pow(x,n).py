# Implement pow(x, n).
#
# Tags: Binary Search, Math
# Difficulty: Medium


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        p = abs(n)
        while p:
            if p & 1:
                result *= x
            p >>= 1
            x *= x

        return result if n >= 0 else 1.0 / result
