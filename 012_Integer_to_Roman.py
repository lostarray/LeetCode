# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.
#
# Tags: Math, String


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        units = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        i = 0
        s = []

        while num > 0:
            u = units[i:i+3]
            num, digit = num / 10, num % 10
            a, b = digit / 5, digit % 5

            if b == 4:
                s.insert(0, u[a+1])
                s.insert(0, u[0])
            else:
                s.insert(0, u[0] * b)
                if a == 1:
                    s.insert(0, u[1])

            i += 2

        return ''.join(s)
