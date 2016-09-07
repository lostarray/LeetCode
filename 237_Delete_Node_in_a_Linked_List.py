# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3,
# the linked list should become 1 -> 2 -> 4 after calling your function.
#
# Tags: Linked List
# Difficulty: Easy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p, q = node, node.next
        while 1:
            p.val = q.val
            if not q.next:
                p.next = None
                break
            p, q = q, q.next
