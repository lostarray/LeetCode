# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern
# and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters
# separated by a single space.
#
# Tags: Hash Table
# Difficulty: Easy


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = str.split()
        if len(l) != len(pattern):
            return False

        map1, map2 = {}, {}

        for i in xrange(len(pattern)):
            p, w = pattern[i], l[i]
            if p not in map1 and w not in map2:
                map1[p] = w
                map2[w] = p
            elif map1.get(p) == w and map2.get(w) == p:
                continue
            else:
                return False

        return True
