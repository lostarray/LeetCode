# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.
#
# Tags: Math, String


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        units = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        last_num = 1000

        for c in s:
            n = units[c]
            if n > last_num:
                sum += n - last_num - last_num
            else:
                sum += n
            last_num = n

        return sum
