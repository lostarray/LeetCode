# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Tags: Linked List, Math


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = tail = None
        end = ListNode(0)
        end.next = end

        while l1 != end or l2 != end or carry != 0:
            sum = l1.val + l2.val + carry
            digit = sum % 10
            carry = sum // 10

            sum_node = ListNode(digit)
            if tail is None:
                head = tail = sum_node
            else:
                tail.next = sum_node
                tail = sum_node

            l1 = l1.next if l1.next else end
            l2 = l2.next if l2.next else end

        return head
