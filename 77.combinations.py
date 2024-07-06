#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (70.56%)
# Likes:    8185
# Dislikes: 222
# Total Accepted:    918K
# Total Submissions: 1.3M
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers
# chosen from the range [1, n].
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to
# be the same combination.
# 
# 
# Example 2:
# 
# 
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 1 <= k <= n
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        cur = []
        ans = []
        self.dfs(n, k, 1, cur, ans)
        return ans

    def dfs(self, n, k, num, cur, ans):
        if (len(cur)==k):
            ans.append(cur[:])
            return

        for i in range(num, n+1):
            # print(i)
            cur.append(i)
            # print(f"cur{cur}")
            self.dfs(n, k, i+1, cur, ans)
            cur.pop()



# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    # output = sol.combine(4, 2)
    output = sol.combine(1, 1)
    print(f"output:{output}")

    # 27/27 cases passed (674 ms)
    # Your runtime beats 88.33 % of python3 submissions
    # Your memory usage beats 23.63 % of python3 submissions (64.8 MB)