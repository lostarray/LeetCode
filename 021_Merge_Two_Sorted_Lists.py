# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Tags: Linked List


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = tail = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next

        tail.next = l1 or l2
        return head.next
