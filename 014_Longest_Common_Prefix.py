# Write a function to find the longest common prefix string amongst an array of strings.
#
# Tags: String


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        size = len(strs)
        if size == 0:
            return ''
        elif size == 1:
            return strs[0]

        i = 0
        while 1:
            try:
                c = strs[0][i]
                for j in xrange(1, size):
                    if strs[j][i] != c:
                        return strs[0][:i]
                i += 1

            except IndexError:
                return strs[0][:i]
