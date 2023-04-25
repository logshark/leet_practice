#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

from typing import List

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        lastIdx = 0
        lastValue = -9999

        for v in nums:
            if v != lastValue:
                lastValue = v
                nums[lastIdx] = v
                lastIdx+=1

        return lastIdx

# @lc code=end

if __name__ == '__main__':
    output = Solution.removeDuplicates(Solution, [1,1,2])

    print(output)