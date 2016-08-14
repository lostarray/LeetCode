# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
#
# Tags: String


class Solution(object):
    def longestPalindrome(self, s):
        """
        Expand around center, O(n^2).

        :type s: str
        :rtype: str
        """
        max_len = 0
        start = end = 0

        for i in xrange(len(s)):
            l1, r1 = self.expand_around_center(s, i, i)
            l2, r2 = self.expand_around_center(s, i, i+1)
            len1 = r1 - l1 + 1
            len2 = r2 - l2 + 1

            if len1 > max_len:
                start, end = l1, r1
                max_len = len1
            if len2 > max_len:
                start, end = l2, r2
                max_len = len2

        return s[start:end+1]

    @staticmethod
    def expand_around_center(s, left, right):
        len_s = len(s)
        while left >= 0 and right < len_s and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1

    def longestPalindrome1(self, s):
        """
        Dynamic Programming, O(n^2).
        Time limit exceeded, but could be accepted if written in C.

        :type s: str
        :rtype: str
        """
        len_s = len(s)
        if len_s == 1 or (len_s == 2 and s[0] == s[1]):
            return s

        left = right = 0
        p1 = [True] * len_s
        p2 = [False] * len_s
        p3 = [False] * len_s
        for i in xrange(len_s - 1):
            if s[i] == s[i+1]:
                p2[i] = True
                left = i
                right = i + 1

        len_p = 3
        while len_p <= len_s:
            for i in xrange(len_s - len_p + 1):
                if p1[i+1] and s[i] == s[i+len_p-1]:
                    p3[i] = True
                    left = i
                    right = i + len_p - 1
                else:
                    p3[i] = False

            p1, p2, p3 = p2, p3, p1
            len_p += 1

        return s[left:right+1]
