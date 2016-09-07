# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
#
# Tags: Tree, Depth-first Search
# Difficulty: Easy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []

        path = []
        result = []
        self.dfs(root, path, result)
        return result

    def dfs(self, node, path, result):
        path.append(str(node.val))

        if not (node.left or node.right):
            result.append('->'.join(path))
        else:
            if node.left:
                self.dfs(node.left, path, result)
            if node.right:
                self.dfs(node.right, path, result)

        path.pop()
