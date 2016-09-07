# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the difference between i and j is at most k.
#
# Tags: Array, Hash Table
# Difficulty: Easy


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i
        return False
