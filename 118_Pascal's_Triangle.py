# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
# Tags: Array
# Difficulty: Easy


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows < 1:
            return result

        result.append([1])
        for i in xrange(1, numRows):
            last_row = result[-1]
            row = [1]

            for j in xrange(i-1):
                row.append(last_row[j] + last_row[j+1])

            row.append(1)
            result.append(row)

        return result


if __name__ == '__main__':
    print Solution().generate(5)
