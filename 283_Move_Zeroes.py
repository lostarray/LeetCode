# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
# Tags: Array, Two Pointers
# Difficulty: Easy


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)

        z = 0
        while z < len_nums and nums[z] != 0:
            z += 1
        if z == len_nums:
            return

        i = z + 1
        while i < len_nums:
            if i < z or nums[i] == 0:
                i += 1
                continue

            nums[z], nums[i] = nums[i], 0
            z += 1
            while nums[z] != 0:
                z += 1
