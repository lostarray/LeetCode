# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three",
# it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37
#
# Tags: String
# Difficulty: Easy


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = [int(v) for v in version1.split('.')]
        ver2 = [int(v) for v in version2.split('.')]

        while ver1 and ver1[-1] == 0:
            ver1.pop()
        while ver2 and ver2[-1] == 0:
            ver2.pop()

        len1 = len(ver1)
        len2 = len(ver2)
        i = -1

        for i in xrange(min(len1, len2)):
            v1 = ver1[i]
            v2 = ver2[i]
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        if i < len1 - 1:
            return 1
        elif i < len2 - 1:
            return -1
        else:
            return 0
