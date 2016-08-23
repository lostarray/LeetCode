# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# You may not alter the values in the nodes, only nodes itself may be changed.
#
# Only constant memory is allowed.
#
# For example,
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Tags: Linked List


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        cur_dummy, cur = dummy, head
        length = 0

        while cur:
            next_cur = cur.next
            length = (length + 1) % k

            if length == 0:
                next_dummy = cur_dummy.next
                self.reverse(cur_dummy, cur.next)
                cur_dummy = next_dummy

            cur = next_cur

        return dummy.next

    def reverse(self, begin, end):
        first = begin.next
        cur = first.next

        while cur != end:
            first.next = cur.next
            cur.next = begin.next
            begin.next = cur
            cur = first.next

    def reverseKGroup1(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k < 2:
            return head

        h = ListNode(0)
        h.next = head

        p = [h]
        try:
            while len(p) < k + 1:
                p.append(p[-1].next)

            while p[-1]:
                q = p[-1:0:-1]
                p[0].next = p[-1]
                p[1].next = p[-1].next
                for i in xrange(2, k+1):
                    p[i].next = p[i-1]

                q.append(p[1].next)
                for _ in xrange(1, k):
                    for i in xrange(len(q)):
                        q[i] = q[i].next

                p = q

        except AttributeError:
            pass

        return h.next


if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5

    s = Solution()
    r = s.reverseKGroup(p1, 3)
    while 1:
        print r.val,
        r = r.next
        if not r:
            break
