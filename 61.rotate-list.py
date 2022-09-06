#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (34.89%)
# Likes:    6212
# Dislikes: 1306
# Total Accepted:    624K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, rotate the list to the right by k places.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#
#
# Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        temp = head
        nodeCnt = 1
        while temp.next != None:
            temp = temp.next
            nodeCnt += 1

        lastNode = temp
        # print(nodeCnt)
        # print(k)
        lastIdxAfterRotated = (nodeCnt - k) % nodeCnt
        # print(lastIdxAfterRotated)

        lastNode.next = head

        while lastIdxAfterRotated:
            lastNode = lastNode.next
            lastIdxAfterRotated -= 1

        head = lastNode.next
        lastNode.next = None

        return head

# @lc code=end

