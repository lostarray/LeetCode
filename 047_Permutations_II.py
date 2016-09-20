# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#
# Tags: Backtracking
# Difficulty: Medium


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        used = [False] * len(nums)
        permutation = []
        self._permute(nums, result, used, permutation)
        return list(result)

    def _permute(self, nums, result, used, permutation):
        if len(permutation) == len(nums):
            result.append(permutation[:])
            return

        for i in xrange(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue

            permutation.append(nums[i])
            used[i] = True
            self._permute(nums, result, used, permutation)
            used[i] = False
            permutation.pop()
