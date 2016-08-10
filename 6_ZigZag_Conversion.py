# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#
# Tags: String


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ''

        zigzag = [[] for _ in xrange(numRows)]
        len_s = len(s)
        i = 0

        while 1:
            row = 0
            while row < numRows:
                zigzag[row].append(s[i])
                row += 1
                i += 1
                if i == len_s:
                    return ''.join(''.join(z) for z in zigzag)

            row = numRows - 2
            while row > 0:
                zigzag[row].append(s[i])
                row -= 1
                i += 1
                if i == len_s:
                    return ''.join(''.join(z) for z in zigzag)


if __name__ == '__main__':
    s = Solution()
    assert s.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
