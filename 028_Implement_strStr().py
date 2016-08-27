# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Tags: Two Pointers, String


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        len_needle = len(needle)
        max_index = len(haystack) - len_needle
        index = 0

        while index <= max_index:
            i, j = index, 0
            while j < len_needle:
                if haystack[i] != needle[j]:
                    break
                i += 1
                j += 1
            else:
                return index

            index += 1

        return -1
