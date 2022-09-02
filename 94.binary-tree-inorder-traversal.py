#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # print(root)
        if root != None:
            self.inorder(root, result)

        return result

    def inorder(self, node: TreeNode, result: List[int]) -> None:
        if node != None:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)
        else:
            return

        return

# @lc code=end

