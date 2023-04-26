#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start

# %%
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # 3 <= nums.length <= 500
        # -1000 <= nums[i] <= 1000
        # -104 <= target <= 104

        nums.sort()
        # print(nums)
        answer = 0
        differ = 10 ** 4 + 1000*3 + 1
        # print("target:%d" %(target))

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            # print("idx i:%d left:%d right:%d" %(i, left, right))
            # print("val i:%d left:%d right:%d" %(nums[i], nums[left], nums[right]))

            while(left < right):
                sum = nums[i] + nums[left] + nums[right]
                # if sum - target

                if (sum > target):
                    tempDiffer = sum - target
                    right-=1
                else:
                    tempDiffer = target - sum
                    left += 1

                # print("sum:%d tempDiffer:%d differ:%d" %(sum, tempDiffer, differ))

                if tempDiffer < differ:
                    differ = tempDiffer
                    answer = sum
                    # print("answer:%d" %answer)

        return answer
# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    # output = sol.threeSumClosest([-1,2,1,-4], 1)
    # output = sol.threeSumClosest([0,0,0,0,0], 0)
    # output = sol.threeSumClosest([1,1,1,0], 100)
    # output = sol.threeSumClosest([-5, -5, -4, 0, 0, 3, 3, 4, 5], -2)
    output = sol.threeSumClosest([-1000,-1000,-1000], 10000)

    print("answer:" + str(output))