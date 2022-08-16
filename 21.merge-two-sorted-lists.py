#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        node1 = list1
        node2 = list2

        result = ListNode()
        temp = result

        while node1 and node2:
            if node1.val < node2.val:
                # print(node1.val)
                temp.next = node1
                node1 = node1.next
            else:
                # print(node2.val)
                temp.next = node2
                node2 = node2.next

            temp = temp.next

        while node1:
            temp.next = node1
            node1 = node1.next
            temp = temp.next

        while node2:
            temp.next = node2
            node2 = node2.next
            temp = temp.next

        return result.next
# @lc code=end

