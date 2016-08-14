# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container.
#
# Tags: Array, Two Pointers


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i, j = 0, len(height) - 1

        while i < j:
            hi, hj = height[i], height[j]
            area = min(hi, hj) * (j - i)
            if area > max_area:
                max_area = area

            if hi < hj:
                i += 1
            else:
                j -= 1

        return max_area
