# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Tags: Array, Pointers


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        min_diff = 0x80000000
        nums.sort()
        length = len(nums)

        for i in xrange(length - 2):
            # important for saving time
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i + 1, length - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                diff = abs(sum - target)

                # important for saving time
                if diff == 0:
                    return sum

                if diff < min_diff:
                    min_diff = diff
                    result = sum

                if sum < target:
                    j += 1
                else:
                    k -= 1

        return result
