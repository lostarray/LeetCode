# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.
#
# Tags: Linked List
#


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        h = ListNode(0)
        h.next = head

        p, q, r = h, head, head.next
        while r:
            p.next = r
            q.next = r.next
            r.next = q

            p, q, r = p.next, r.next, q.next
            if not r:
                break
            p, q, r = p.next, q.next, r.next

        return h.next
