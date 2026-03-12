#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start

# %%
from typing import List
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        answers = []
        candidates.sort()
        self.combination(answers, 0, candidates,[])
        return answers

    def combination(self, answers, i, candidates, output):
        print("combination")

        if(len(output) >= len(candidates)):
            # output.pop()
            # answers.append(output.copy())
            return

        for i in range(i, len(candidates)):
            output.append(candidates[i])
            answers.append(output.copy())
            print(output)
            self.combination(answers, i+1, candidates, output)
            output.pop()


        print("combination end")
        pass

    # answers = []

    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

    #     candidates.sort()
    #     self.combination([], candidates,target)
    #     return self.answers

    # def combination(self, answer, candidates, target):
    #     print("combination")
    #     for i in candidates:
    #         print("target:%d i:%d" %(target, i))
    #         # print(i)
    #         temp = target - i
    #         if (temp) < 0:
    #            print("temp:%d < 0" %(temp))
    #            answer.pop(-1)
    #            return

    #         answer.append(i)
    #         if temp == 0:
    #             print("temp:%d == 0" %(temp))
    #             print(answer)
    #             self.answers.append(answer.copy())
    #             print(self.answers)
    #             answer.pop(-1)
    #             # answer = []
    #             return
    #         else:
    #             print("temp:%d >= 0" %(temp))
    #             self.combination(answer,candidates, target-i)

    #     print("combination end")
    #     pass



# @lc code=end

# if __name__ == '__main__':

# input = [2,3,6,7]

input = [1,2,3]
target = 7
solution = Solution()
output = solution.combinationSum(input, target)
print(output)

# %%
