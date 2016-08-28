# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.
#
# Tags: String
# Difficulty: Easy


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in xrange(1, n):
            t = []
            last_c = None
            count = 0

            for i in xrange(len(s)):
                c = s[i]
                if c == last_c:
                    count += 1
                else:
                    if last_c:
                        t.append(str(count))
                        t.append(last_c)
                    count = 1
                    last_c = c

            if last_c:
                t.append(str(count))
                t.append(last_c)

            s = ''.join(t)

        return s


if __name__ == '__main__':
    print Solution().countAndSay(2)
