# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.
#
# Tags: Math
# Difficulty: Easy


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            count = n / 5
            n = count
            result += count
        return result
