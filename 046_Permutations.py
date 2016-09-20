# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
# Tags: Backtracking
# Difficulty: Medium


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        indices = []
        self._permute(nums, result, indices)
        return result

    def _permute(self, nums, result, indices):
        if len(indices) == len(nums):
            result.append([nums[i] for i in indices])
            return

        for i in xrange(len(nums)):
            if i not in indices:
                indices.append(i)
                self._permute(nums, result, indices)
                indices.pop()
