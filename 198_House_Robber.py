# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
# money you can rob tonight without alerting the police.
#
# Tags: Dynamic Programming
# Difficulty: Easy


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        num_i = max(nums[0], nums[1])
        num_i_1 = nums[0]

        for i in xrange(2, len(nums)):
            num_i_2, num_i_1 = num_i_1, num_i
            num_i = max(num_i_2 + nums[i], num_i_1)

        return num_i
