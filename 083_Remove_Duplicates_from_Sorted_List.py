# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
#
# Tags: Linked List
# Difficulty: Easy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        p, q = head, head.next
        while q:
            if p.val == q.val:
                q = q.next
                p.next = q
            else:
                p, q = q, q.next
        return head
