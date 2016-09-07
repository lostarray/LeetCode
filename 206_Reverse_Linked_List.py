# Reverse a singly linked list.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
#
# Tags: Linked List
# Difficulty: Easy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        p, q = head, head.next
        head.next = None

        while q:
            t, p, q = p, q, q.next
            p.next = t

        return p
