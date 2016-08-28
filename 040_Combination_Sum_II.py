# Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
# Tags: Array, Backtracking
# Difficulty: Medium


class Solution(object):
    def combinationSum2(self, candidates, target):
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

        prev_num = 0
        while index < len(candidates):
            candidate = candidates[index]
            if target < candidate:
                break

            if candidate != prev_num:
                chosen.append(candidate)
                self.combine(candidates, target - candidate, result, chosen, index + 1)
                chosen.pop()
                prev_num = candidate

            index += 1


if __name__ == '__main__':
    print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
