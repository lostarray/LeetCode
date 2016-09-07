# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
# Hint:
#
# A naive implementation of the above process is trivial. Could you come up with other methods?
# What are all the possible results?
# How do they occur, periodically or randomly?
# You may find this Wikipedia[https://en.wikipedia.org/wiki/Digital_root] article useful.
#
# Tags: Math
# Difficulty: Easy


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            dr, n = 0, num
            while n > 0:
                n, mod = n / 10, n % 10
                dr += mod
            num = dr
        return num
