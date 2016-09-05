# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
#
# Tags: Array
# Difficulty: Easy


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in xrange(rowIndex):
            for j in xrange(i, 0, -1):
                row[j] += row[j-1]
            row.append(1)
        return row

    def getRow1(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = last_row = [1]

        for i in xrange(1, rowIndex + 1):
            row = [1]

            for j in xrange(i-1):
                row.append(last_row[j] + last_row[j+1])

            row.append(1)
            last_row = row

        return row


if __name__ == '__main__':
    print Solution().getRow(3)
