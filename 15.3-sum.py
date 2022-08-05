#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answers = []
        
        elements = len(nums)
        for i in range(elements):
            for j in range(i+1, elements):
                for k in range(j+1, elements):
                    # print(str(i) + " " + str(j) + " " + str(k))
                    if ((nums[i] + nums[j] + nums[k]) == 0):
                        temp = sorted([nums[i],nums[j],nums[k]])
                        # print(temp)
                        if answers:
                            insert = True
                            for answer in answers:
                                # if sorted(answer) == sorted(temp):
                                if answer == temp:
                                    insert = False
                                    break
                            
                            if insert:
                                answers.append(temp) 
                            
                        else:
                            answers.append(temp) 
                            
        return answers
# @lc code=end

