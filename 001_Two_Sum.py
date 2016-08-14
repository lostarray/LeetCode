# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
# Tags: Array, Hash Table


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i in xrange(len(nums)):
            a = nums[i]
            b = target - a
            if b in index:
                return [index[b], i]
            index[a] = i

    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        for i in xrange(size):
            for j in xrange(i + 1, size):
                if nums[i] + nums[j] == target:
                    return [i, j]
