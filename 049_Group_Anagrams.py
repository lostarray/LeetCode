# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.
#
# Tags: Hash Table, String
# Difficulty: Medium

import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ht = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            ht[key].append(s)
        return ht.values()
