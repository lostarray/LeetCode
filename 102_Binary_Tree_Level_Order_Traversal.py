# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
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
    def levelOrder(self, root):
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
                result.append(row)

        return result
