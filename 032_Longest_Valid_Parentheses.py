# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
#
# Tags: Dynamic Programming, String
# Difficulty: Hard


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        last_invalid = -1
        indices = []

        for i in xrange(len(s)):
            if s[i] == '(':
                indices.append(i)
            elif not indices:
                last_invalid = i
            else:
                indices.pop()
                if indices:
                    longest = max(longest, i - indices[-1])
                else:
                    longest = max(longest, i - last_invalid)

        return longest
