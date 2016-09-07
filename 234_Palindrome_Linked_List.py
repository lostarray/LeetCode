# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# Tags: Linked List, Two Pointers
# Difficulty: Easy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        reverse = None

        while fast and fast.next:
            fast = fast.next.next
            head.next, head, reverse = reverse, head.next, head

        tail = head.next if fast else head
        pal = True
        while reverse:
            pal = pal and tail.val == reverse.val
            tail = tail.next
            reverse.next, reverse, head = head, reverse.next, reverse

        return pal


if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(2)
    h.next.next.next.next = ListNode(1)
    print Solution().isPalindrome(h)
