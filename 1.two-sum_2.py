#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = dict()

        for i in range(len(nums)):
            if nums_dic.__contains__(target-nums[i]):
                return nums_dic.get(target-nums[i]), i
            else:
                nums_dic[nums[i]] = i

# @lc code=end

