#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # print(root)
        if root != None:
            self.postorder(root, result)

        return result

    def postorder(self, node: TreeNode, result: List[int]) -> None:
        if node != None:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.val)
        else:
            return

        return
# @lc code=end

