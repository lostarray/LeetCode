# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#
# Tags: Math
# Difficulty: Easy


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        base = ord('A') - 1

        for c in s:
            n = ord(c) - base
            result = result * 26 + n

        return result
