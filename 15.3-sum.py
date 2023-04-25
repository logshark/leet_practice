#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # input
        # [-1,0,1,2,-1,-4]

        # sorted input
        # [-4,-1,-1,0,1,2]

        answers = []
        nums.sort()
        print(nums)

        for i in range(len(nums) - 2):
            # print(nums[i])
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    answers.append([nums[i], nums[left],nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left +=1

                    while left < right and nums[right] == nums[right-1]:
                        right -=1

                    left += 1
                    right -= 1

        return answers
# @lc code=end

if __name__ == '__main__':
    output = Solution.threeSum(Solution, [-1,0,1,2,-1,-4])
    print(output)


# Accepted
# 312/312 cases passed (1346 ms)
# Your runtime beats 68.85 % of python3 submissions
# Your memory usage beats 21.99 % of python3 submissions (18.6 MB)