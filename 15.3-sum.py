#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # input
        # [-1,0,1,2,-1,-4]

        # sorted input
        # [-4,-1,-1,0,1,2]

        answers = []
        nums.sort()
        # print(nums)

        for i in range(len(nums) - 2):
            # print(nums[i])
            left = i+1
            right = len(nums) - 1

            while left < right:                
                Sum = nums[i] + nums[left] + nums[right]

                if Sum > 0:
                    right -= 1
                elif Sum < 0:
                    left += 1
                else:
                    temp = [nums[i], nums[left],nums[right]]
                    append = True
                    if answers:
                        for answer in answers:
                            if temp == answer:
                                append = False
                                break
                        if append:
                            answers.append(temp)
                    else:
                        answers.append(temp)
                    left += 1
                    if nums[left] == nums[right]:
                        break
                

        return answers
# @lc code=end

