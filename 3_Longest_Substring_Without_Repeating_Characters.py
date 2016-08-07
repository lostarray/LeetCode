# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Tags: Hash Table, Two Pointers, String


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre_location = {}
        len_s = len(s)
        start = end = max_len = 0

        while end < len_s:
            c = s[end]
            loc = pre_location.get(c, -1)
            if start <= loc:
                start = loc + 1

            len_sub = end - start + 1
            if len_sub > max_len:
                max_len = len_sub

            pre_location[c] = end
            end += 1

        return max_len
