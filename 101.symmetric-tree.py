#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (51.57%)
# Likes:    10873
# Dislikes: 254
# Total Accepted:    1.4M
# Total Submissions: 2.6M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Could you solve it both recursively and iteratively?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if root is None:
        #     return None
        # else:
            return self.isSymmetricTree(root.left, root.right)

    def isSymmetricTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None and q == None):
            return True
        elif (p == None and q != None) or (p != None and q == None):
            return False
        else:
            return ((p.val == q.val) and self.isSymmetricTree(p.left, q.right) and self.isSymmetricTree(p.right, q.left))

    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if (p == None and q == None):
    #         return True
    #     elif (p == None and q != None) or (p != None and q == None):
    #         return False
    #     else:
    #         return ((p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))



# @lc code=end

