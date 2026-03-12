#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (54.65%)
# Likes:    10410
# Dislikes: 292
# Total Accepted:    997.9K
# Total Submissions: 1.8M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note: The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Each number in candidates may only be used once in the combination.
        # Note: The solution set must not contain duplicate combinations.
        cur = []
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, cur, result)

        return result
    
    def dfs(self, candidates, target, start, cur, result):

        if target == 0:
            # remove it dut to condition: "if i > start and candidates[i] == candidates[i-1]: continue"
            # if cur not in result: 
            result.append(cur[:])
            
            return

        
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            
            if i > start and candidates[i] == candidates[i-1]:
                continue

            cur.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i+1, cur, result)
            cur.pop()
        return
# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    
    # Time Limit Exceeded
    #   Testcase [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 30
    #   Expected Answer [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    output = sol.combinationSum2([10,1,2,7,6,1,5], 8)
    print(output)

    # 176/176 cases passed (40 ms)
    # Your runtime beats 95.58 % of python3 submissions
    # Your memory usage beats 92.07 % of python3 submissions (16.4 MB)