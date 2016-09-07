# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
# https://leetcode.com/static/images/problemset/rectangle_area.png
#
# Rectangle Area
# Assume that the total area is never beyond the maximum possible value of int.
#
# Tags: Math
# Difficulty: Easy


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        overlap_width = max(0, min(C, G) - max(A, E))
        overlap_height = max(0, min(D, H) - max(B, F))
        return area1 + area2 - overlap_width * overlap_height

    def computeArea1(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if E < A or (E == A and G > C):
            return self.computeArea(E, F, G, H, A, B, C, D)

        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)

        if E >= C or F >= D or H <= B:
            return area1 + area2

        if G <= C and F >= B and H <= D:
            return area1

        width = min(C, G) - E
        height = min(D, H) - max(B, F)
        overlap = width * height
        return area1 + area2 - overlap


if __name__ == '__main__':
    print Solution().computeArea(-2, -2, 2, 2, 1, -3, 3, -1)
