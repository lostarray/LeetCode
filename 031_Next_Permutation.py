# coding: utf-8

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order
# (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
# Tags: Array
# Difficulty: Medium


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        small_i = -1
        for i in xrange(len(nums) - 1):
            if nums[i] < nums[i+1]:
                small_i = i

        if small_i == -1:
            nums.reverse()
            return

        small = nums[small_i]
        large_i = 0

        for i in xrange(small_i + 1, len(nums)):
            if nums[i] > small:
                large_i = i

        nums[small_i], nums[large_i] = nums[large_i], small
        nums[small_i + 1:] = nums[:small_i:-1]
