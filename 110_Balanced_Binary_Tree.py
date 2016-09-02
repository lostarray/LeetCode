# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which
# the depth of the two subtrees of every node never differ by more than 1.
#
# Tags: Tree, Depth-first Search
# Difficulty: Easy


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.maxDepth(root)[0]

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: bool, int
        """
        if not root:
            return True, 0

        left_balanced, left_depth = self.maxDepth(root.left)
        right_balanced, right_depth = self.maxDepth(root.right)
        balanced = left_balanced and right_balanced and abs(left_depth - right_depth) <= 1

        max_depth = max(left_depth, right_depth) + 1 if balanced else 0
        return balanced, max_depth
