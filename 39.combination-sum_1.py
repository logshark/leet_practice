#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (68.72%)
# Likes:    18660
# Dislikes: 411
# Total Accepted:    2M
# Total Submissions: 2.7M
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
#
# The test cases are generated such that the number of unique combinations that
# sum up to target is less than 150 combinations for the given input.
#
#
# Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#
#
# Example 3:
#
#
# Input: candidates = [2], target = 1
# Output: []
#
#
#
# Constraints:
#
#
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
#
#
#


# @lc code=start
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        cur = []
        # candidates.sort()
        self.dfs(candidates, target, cur, 0, result)
        # print(f"final:{result}")
        return result

    def dfs(self, candidates, target, cur, start, result):
        # print(f"target:{target}")
        if target == 0:
            cur_sorted = cur[:]
            cur_sorted.sort()
            if cur_sorted not in result:
                result.append(cur_sorted[:])
            # result.append(cur) #!!!!
            # print(f"result append:{cur}")
            # print(f"result in dfs func:{result}")
            return

        if target < 0:
            return

        for i in range(0, len(candidates)):
            # print(f"i:{i}, candidates:{candidates[i]}, target:{target} cur:{cur}")
            # if candidates[i] > target:
            #     # print("break")
            #     break

            cur.append(candidates[i])
            # print(f"after append cur:{cur}")
            self.dfs(candidates, target - candidates[i], cur, i, result)
            cur.pop()
            # print(f"after pop cur:{cur}, result:{result}")

# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    output = sol.combinationSum([2,3,6,7], 7)
    print(output)

    # 160/160 cases passed (537 ms)
    # Your runtime beats 5 % of python3 submissions
    # Your memory usage beats 33.21 % of python3 submissions (16.6 MB)
