# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".
#
# Tags: Math, String
# Difficulty: Easy


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        ord0 = ord('0')
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0:
            x = ord(a[i]) - ord0 if i >= 0 else 0
            y = ord(b[j]) - ord0 if j >= 0 else 0

            sum = x + y + carry
            carry, n = sum / 2, sum % 2
            result.append(chr(n + ord0))

            i, j = i - 1, j - 1

        if carry:
            result.append('1')

        return ''.join(reversed(result))
