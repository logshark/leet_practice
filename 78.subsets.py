#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (75.02%)
# Likes:    17163
# Dislikes: 281
# Total Accepted:    2M
# Total Submissions: 2.5M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
#
#

# @lc code=start
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, length, start, cur, ans):
            if length == len(cur):
                # print(f"ans:{ans}")
                return

            for i in range(start, len(nums)):
                # print(f"i:{i}")
                cur.append(nums[i])
                ans.append(cur[:])
                # print(f"cur:{cur}")
                dfs(nums, length+1, i+1, cur, ans)
                cur.pop()

        ans = []
        cur = []
        ans.append([])
        dfs(nums, 1, 0, cur, ans)

        return ans
# @lc code=end


if __name__ == '__main__':
    sol = Solution()
    output = sol.subsets([1, 2, 3])
    print(output)
