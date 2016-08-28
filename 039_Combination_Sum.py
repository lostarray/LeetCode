# Given a set of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]
#
# Tags: Array, Backtracking
# Difficulty: Medium


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates = sorted(candidates)
        self.combine(candidates, target, result, [], 0)
        return result

    def combine(self, candidates, target, result, chosen, index):
        if target == 0:
            result.append(chosen[:])

        while index < len(candidates):
            candidate = candidates[index]
            if target < candidate:
                break

            chosen.append(candidate)
            self.combine(candidates, target - candidate, result, chosen, index)
            chosen.pop()
            index += 1


if __name__ == '__main__':
    print Solution().combinationSum([8, 7, 4, 3], 11)
