# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Tags: Hash Table, Bit Manipulation
# Difficulty: Easy


class Solution(object):
    def singleNumber(self, nums):
        """
        Bit Manipulation

        :type nums: List[int]
        :rtype: int
        """
        import operator
        return reduce(operator.xor, nums)

    def singleNumber1(self, nums):
        """
        Hash Table

        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for n in nums:
            if n in s:
                s.discard(n)
            else:
                s.add(n)
        return s.pop()
