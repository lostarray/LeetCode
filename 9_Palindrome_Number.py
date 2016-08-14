# Determine whether an integer is a palindrome. Do this without extra space.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
# you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
#
# Tags: Math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        y = x
        reverse = 0

        while y > 0:
            reverse = reverse * 10 + y % 10
            y /= 10

        return reverse == x

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        length = 0
        n = x
        while n > 0:
            n /= 10
            length += 1

        while length > 1:
            n = 10 ** (length - 1)
            a, b = x / n, x % 10
            if a != b:
                return False

            x = ((x - a * n) - b) / 10
            length -= 2

        return True


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(121)
