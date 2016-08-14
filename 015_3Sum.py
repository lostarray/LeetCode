# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
# Tags: Array, Two Pointers


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()

        nums.sort()
        length = len(nums)

        for i in xrange(length - 2):
            ni = nums[i]
            if i and ni == nums[i-1]:
                continue

            target = -ni
            j, k = i + 1, length - 1

            while j < k:
                nj, nk = nums[j], nums[k]

                if nj + nk == target:
                    result.add((ni, nj, nk))
                    j += 1
                    k -= 1
                elif nj + nk < target:
                    j += 1
                else:
                    k -= 1

        return list(result)
