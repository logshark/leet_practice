#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (53.59%)
# Likes:    7037
# Dislikes: 191
# Total Accepted:    792.3K
# Total Submissions: 1.4M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the zigzag level order traversal of
# its nodes' values. (i.e., from left to right, then right to left for the next
# level and alternate between).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None

        q = []
        q.append(root)
        result = []
        levelCnt = 0

        while q:
            levelQ = []
            # print(len(q))
            for _ in range(len(q)):

                node = q.pop(0)
                # print(node.val)
                levelQ.append(node.val)


                if (node.left) != None:
                    q.append(node.left)
                if (node.right) != None:
                    q.append(node.right)

            if (levelCnt % 2) != 0:
                levelQ.reverse()

            result.append(levelQ)
            levelCnt += 1

        return result
# @lc code=end

