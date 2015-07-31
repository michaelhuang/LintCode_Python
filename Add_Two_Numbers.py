# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        head = ListNode(0)
        point = head
        carry = 0

        while (l1 is not None and
                   l2 is  not None):
            sum = carry + l1.val + l2.val
            point.next = ListNode(sum%10)
            carry = sum / 10
            l1 = l1.next
            l2 = l2.next
            point = point.next

        if l1 is not None:
            l = l1
        else:
            l = l2

        while l is not None:
            sum = carry + l.val
            point.next = ListNode(sum%10)
            carry = sum / 10
            l = l.next
            point = point.next

        if carry <> 0:
            point.next = ListNode(carry)

        return  head.next

if __name__ == '__main__':
    l1 = ListNode(7)
    l1.next = ListNode(1)
    l1.next.next = ListNode(6)
    l2 = ListNode(5)
    l2.next = ListNode(9)
    l2.next.next = ListNode(2)

    a = Solution()
    result = a.addLists(l1, l2)
    while result is not None:
        print result.val
        result = result.next