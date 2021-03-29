#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

from typing import List

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergelist = nums1 + nums2
        mergelist.sort()

        half = len(mergelist) // 2

        if len(mergelist) % 2 == 0:
            return (mergelist[half-1]+mergelist[half]) / 2
        else:
            return mergelist[half]

# @lc code=end

if __name__ == "__main__":

    nums1 = [1, 2]
    nums2 = [3, 4]

    mergelist = nums1 + nums2
    mergelist.sort()

    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))

# 2021/02/24
# Accepted
# 2091/2091 cases passed (92 ms)
# Your runtime beats 71.36 % of python3 submissions
# Your memory usage beats 82.92 % of python3 submissions (14.4 MB)