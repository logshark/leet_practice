#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxContainer = 0
        i = 0
        j = len(height)-1
        
        while(i < j):
            if height[i] < height[j]:
                maxContainer = max(maxContainer, height[i] * (j-i))
                i+=1
            else:
                maxContainer = max(maxContainer, height[j] * (j-i))
                j-=1
        
        return maxContainer
        
# @lc code=end

