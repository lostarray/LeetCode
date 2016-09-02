# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
# Tags: Tree, Breadth-first Search
# Difficulty: Easy


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = [root]

        while queue:
            row = []
            for _ in xrange(len(queue)):
                node = queue.pop(0)
                if not node:
                    continue
                row.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

            if row:
                result.insert(0, row)

        return result
