# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.
#
# Tags: String
# Difficulty: Easy


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        i = len(s) - 1

        while i >= 0:
            if s[i] != ' ':
                length += 1
            elif length:
                break
            i -= 1

        return length


if __name__ == '__main__':
    print Solution().lengthOfLastWord("b   a    ")
