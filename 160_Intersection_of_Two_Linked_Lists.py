# coding: utf-8

# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
# Tags: Linked List
# Difficulty: Easy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Two Pointers

        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        pa, pb = headA, headB
        ta, tb = None, None

        while pa and pb:
            if pa == pb:
                return pa

            if pa.next:
                pa = pa.next
            elif not ta:
                ta = pa
                pa = headB
            else:
                break

            if pb.next:
                pb = pb.next
            elif not tb:
                tb = pb
                pb = headA
            else:
                break

    def getIntersectionNode1(self, headA, headB):
        """
        Hash Table, Memory Limit Exceeded

        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        s = set()
        p = headA
        while p:
            s.add(p)
            p = p.next

        p = headB
        while p:
            if p in s:
                return p
            p = p.next

        return None
