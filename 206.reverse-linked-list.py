#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return

        preNode = None
        curNode = head
        nxtNode = curNode.next

        while nxtNode != None:
            # print(curNode.val)
            curNode.next = preNode
            preNode = curNode
            curNode = nxtNode
            nxtNode = nxtNode.next

        curNode.next = preNode

        return curNode


# @lc code=end

