#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # reference: https://ithelp.ithome.com.tw/articles/10223721

        if head == None or head.next == None:
            return None

        if head.next == head:
            return head

        oneStep = head
        twoStep = head

        while twoStep != None and twoStep.next != None:
            oneStep = oneStep.next
            twoStep = twoStep.next.next

            if twoStep == oneStep:
                # print(oneStep.val)
                oneStep2 = head
                while oneStep != oneStep2:
                    oneStep = oneStep.next
                    oneStep2 = oneStep2.next
                return oneStep

            # print("loopD")

        return None
# @lc code=end

