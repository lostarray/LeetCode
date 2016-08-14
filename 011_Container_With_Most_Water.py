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
        size = len(height)
        i, j = 0, size - 1
        hi, hj = height[i], height[j]
        max_area = min(hi, hj) * (j - i)

        direction = 1 if hi <= hj else -1
        t = i + 1 if direction > 0 else j - 1

        while i < t < j:
            ht = height[t]
            if direction > 0 and ht <= hi:
                t += 1
                continue
            elif direction < 0 and ht <= hj:
                t -= 1
                continue

            left_area = min(hi, ht) * (t - i)
            right_area = min(hj, ht) * (j - t)
            max_area = max(max_area, left_area, right_area)

            if direction > 0 and ht > hj:
                direction = -1
                i = t
                hi = height[i]
                t = j - 1
            elif direction < 0 and ht > hi:
                direction = 1
                j = t
                hj = height[j]
                t = i + 1
            else:
                t += direction

        return max_area
