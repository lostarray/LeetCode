# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#
# Tags: Array, Hash Table, Two Pointers


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import collections

        nums.sort()
        length = len(nums)

        ht = collections.defaultdict(set)
        for i in xrange(length - 1):
            for j in xrange(i+1, length):
                ht[nums[i] + nums[j]].add((i, j))

        ret = set()
        for i in xrange(2, length-1):
            for j in xrange(i+1, length):
                remain = target - nums[i] - nums[j]
                if remain in ht:
                    for a, b in ht[remain]:
                        if b < i:
                            ret.add((nums[a], nums[b], nums[i], nums[j]))

        return list(ret)

    def fourSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = set()
        nums.sort()
        length = len(nums)

        for i in xrange(length - 3):
            for j in xrange(i + 1, length - 2):
                remain = target - nums[i] - nums[j]
                k, l = j + 1, length - 1
                while k < l:
                    sum = nums[k] + nums[l]
                    if nums[k] + nums[l] == remain:
                        ret.add((nums[i], nums[j], nums[k], nums[l]))
                    if sum < remain:
                        k += 1
                    else:
                        l -= 1

        return list(ret)