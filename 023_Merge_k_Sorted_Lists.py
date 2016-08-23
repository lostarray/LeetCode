# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Tags: Divide and Conquer, Linked List, Heap


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        while len(lists) > 1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            m = self.mergeTwoLists(l1, l2)
            lists.append(m)

        return lists[0]

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
