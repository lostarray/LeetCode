# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
# Note:
# The numbers can be arbitrarily large and are non-negative.
# Converting the input string to integer is NOT allowed.
# You should NOT use internal library such as BigInteger.
#
# Tags: Math, String
# Difficulty: Medium


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        for i in xrange(len(num1) - 1, -1, -1):
            n1 = int(num1[i])
            for j in xrange(len(num2) - 1, -1, -1):
                index = i + j + 1
                n2 = int(num2[j])
                n = n1 * n2 + result[index]
                carry, digit = n / 10, n % 10
                result[index] = digit
                result[index - 1] += carry

        for i in xrange(len(result)):
            if result[i] != 0:
                break

        return ''.join(str(d) for d in result[i:])
