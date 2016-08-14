# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases.
# If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
#
# Requirements for atoi:
#
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found.
# Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digits as possible,
# and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values,
# INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
#
# Tags: Math, String


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = 0
        negative = False

        convert_started = False
        ord_0 = ord('0')

        for c in str.lstrip():
            if convert_started:
                n = ord(c) - ord_0
                if 0 <= n <= 9:
                    num = num * 10 + n
                else:
                    break

            else:
                n = ord(c) - ord_0
                if c == '-':
                    negative = True
                elif 0 <= n <= 9:
                    num = n
                elif c != '+':
                    break
                convert_started = True

        int_max = 0x7FFFFFFF
        int_min = -0x80000000

        if negative:
            num = -num
            return int_min if num < int_min else num
        else:
            return int_max if num > int_max else num


if __name__ == '__main__':
    s = Solution()
    print s.myAtoi('+1')
