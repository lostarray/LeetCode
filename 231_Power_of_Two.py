# Given an integer, write a function to determine if it is a power of two.
#
# Tags: Math, Bit Manipulation
# Difficulty: Easy


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0
