# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
# Tags: Binary Search, Array, Divide and Conquer

import collections


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = collections.deque()
        len1, len2 = len(nums1), len(nums2)
        i = j = 0

        while i < len1 and j < len2:
            n1, n2 = nums1[i], nums2[j]
            if n1 < n2:
                nums.append(n1)
                i += 1
            else:
                nums.append(n2)
                j += 1

        if i == len1:
            nums.extend(nums2[j:])
        else:
            nums.extend(nums1[i:])

        len_sum = len1 + len2
        mid = len_sum // 2

        if len_sum % 2 == 0:
            return float(nums[mid-1] + nums[mid]) / 2
        else:
            return nums[mid]
