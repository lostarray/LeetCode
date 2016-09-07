# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
#
# Note that 1 is typically treated as an ugly number.
#
# Tags: Math
# Difficulty: Easy


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        factors = [2, 3, 5]
        i = 0
        factor = factors[i]

        while num > 1:
            if num % factor == 0:
                num /= factor
            else:
                i += 1
                if i >= len(factors):
                    return False
                factor = factors[i]

        return True
