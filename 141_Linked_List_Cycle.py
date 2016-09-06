# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?
#
# Tags: Linked List, Two Pointers
# Difficulty: Easy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        fast = slow = head
        while 1:
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
            if fast is None:
                return False

            slow = slow.next
            if slow is None:
                return False

            if fast == slow:
                return True
