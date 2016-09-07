# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which will return whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.
#
# Tags: Binary Search
# Difficulty: Easy


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return True if version >= 4 else False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while 1:
            mid = (left + right) / 2
            if mid == right:
                break

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return right


if __name__ == '__main__':
    print Solution().firstBadVersion(100)
