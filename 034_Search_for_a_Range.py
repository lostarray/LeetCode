# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
#
# Tags: Binary Search, Array
# Difficulty: Medium


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index, left, right = self.binary_search(nums, target, 0, len(nums) - 1)
        if index < 0:
            return [-1, -1]

        l, i = left, index
        while nums[l] != target:
            l += 1
            i, l, _ = self.binary_search(nums, target, l, i)
        left = l

        r, i = right, index
        while nums[r] != target:
            r -= 1
            i, _, r = self.binary_search(nums, target, i, r)
        right = r

        return [left, right]

    def binary_search(self, nums, target, left, right):
        index = -1

        while left <= right:
            mid = (left + right) / 2

            if nums[mid] == target:
                index = mid
                break

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return index, left, right


if __name__ == '__main__':
    print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
