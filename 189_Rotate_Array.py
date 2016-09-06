# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
# Hint:
# Could you do it in-place with O(1) extra space?
# Related problem: Reverse Words in a String II
#
# Tags: Array
# Difficulty: Easy


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m = len(nums) - k
        nums[:k], nums[k:] = nums[m:], nums[:m]

    def rotate1(self, nums, k):
        """
        :type nums: List
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for _ in xrange(k):
            nums.insert(0, nums.pop())
