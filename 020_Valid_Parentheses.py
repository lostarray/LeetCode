# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
#
# Tags: Stack, String


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if stack and pair.get(stack[-1]) == c:
                stack.pop()
            else:
                stack.append(c)

        return not stack
