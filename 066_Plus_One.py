# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# Tags: Array, Math
# Difficulty: Easy


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        carry = 1

        for d in reversed(digits):
            sum = d + carry
            carry, n = sum / 10, sum % 10
            result.insert(0, n)

        if carry:
            result.insert(0, carry)

        return result
