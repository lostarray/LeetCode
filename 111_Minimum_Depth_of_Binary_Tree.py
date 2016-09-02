# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Tags: Tree, Depth-first Search, Breadth-first Search
# Difficulty: Easy


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = [root]
        depth = 0
        stop = False

        while queue:
            for _ in xrange(len(queue)):
                node = queue.pop(0)
                if not (node.left or node.right):
                    stop = True
                    break

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1
            if stop:
                break

        return depth
