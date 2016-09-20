# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].
#
# Tags: Array
# Difficulty: Medium


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result

        m = len(matrix)
        n = len(matrix[0])
        size = m * n
        up, down, left, right = 0, m - 1, 0, n - 1

        while len(result) < size:
            for j in xrange(left, right + 1):
                result.append(matrix[up][j])
            up += 1

            for i in xrange(up, down + 1):
                result.append(matrix[i][right])
            right -= 1

            if up > down or left > right:
                break

            for j in xrange(right, left - 1, -1):
                result.append(matrix[down][j])
            down -= 1

            for i in xrange(down, up - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result


if __name__ == '__main__':
    print Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
