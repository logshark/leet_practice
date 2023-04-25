#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        head = current = ListNode()
        carry = 0

        while(l1 and l2):
            current.val = l1.val+l2.val + carry
            if current.val >= 10:
                current.val -= 10
                carry = 1
            else:
                carry = 0

            # print(current.val, end = " ")
            # print(carry)

            if l1.next and l2.next:
                next = ListNode()
                current.next = next
                current = current.next

            l1 = l1.next
            l2 = l2.next

        if l1:
            # print("if l1")
            current.next = l1

        if l2:
            # print("if l2")
            current.next = l2

        while carry:
            if current.next:
                current = current.next
                current.val += carry
                if current.val >= 10:
                    current.val -= 10
                    carry = 1
                else:
                    carry = 0
            else:
                # print("else")
                current.next = ListNode(1)
                carry = 0

        return head

# @lc code=end

if __name__ == '__main__':

    l1 = ListNode(9, ListNode(9))
    l2 = ListNode(9, ListNode(9, ListNode(9)))

    output = Solution.addTwoNumbers(Solution, l1,l2)
    print("output")
    while(output):
        print(output.val, end=" ")
        output = output.next
