# coding: utf-8

# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Tags: Array, Divide and Conquer, Bit Manipulation
# Difficulty: Easy


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        demand = len(nums) / 2
        for num, count in d.iteritems():
            if count > demand:
                return num
