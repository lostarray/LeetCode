# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.
#
# Tags: Math, Binary Search


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend < 0:
            if divisor < 0:
                result = self.divide_positive(-dividend, -divisor)
            else:
                result = -self.divide_positive(-dividend, divisor)
        else:
            if divisor < 0:
                result = -self.divide_positive(dividend, -divisor)
            else:
                result = self.divide_positive(dividend, divisor)

        max_int = 0x7FFFFFFF
        return result if result <= max_int else max_int

    def divide_positive(self, dividend, divisor):
        if dividend < divisor:
            return 0

        d = divisor
        half = 0
        result = 1

        while 1:
            d += d
            if dividend < d:
                break
            half = d
            result += result

        if half == 0:
            return result

        remain = dividend - half
        return self.divide_positive(remain, divisor) + result


if __name__ == '__main__':
    print Solution().divide(10, 3)
