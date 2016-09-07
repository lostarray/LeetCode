# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.
#
# Tags: Hash Table
# Difficulty: Easy


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2t, t2s = {}, {}

        for i in xrange(len(s)):
            cs, ct = s[i], t[i]

            if cs not in s2t and ct not in t2s:
                s2t[cs] = ct
                t2s[ct] = cs

            elif cs not in s2t or s2t[cs] != ct:
                return False

        return True
