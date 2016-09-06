# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#
# Tags: Math
# Difficulty: Easy


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        l = []
        base = ord('A')

        while n > 0:
            n -= 1
            mod = n % 26
            l.insert(0, chr(base + mod))
            n /= 26

        return ''.join(l)


if __name__ == '__main__':
    s = Solution()
    print s.convertToTitle(1)
    print s.convertToTitle(26)
    print s.convertToTitle(27)
