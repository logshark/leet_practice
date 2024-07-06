#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (60.65%)
# Likes:    18388
# Dislikes: 992
# Total Accepted:    2.1M
# Total Submissions: 3.4M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
# Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
#
#

# @lc code=start
from typing import List


class Solution:
    digitsToLetter = {'2': ['a','b','c'], '3': ['d','e','f'] , '4': ['g','h','i'] , '5': ['j','k','l'] ,
                    '6': ['m','n','o'], '7': ['p','q','r', 's'], '8': ['t','u','v'] , '9': ['w','x','y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        result = []
        self.bfs(digits, 0, "", result)
        return result

    def bfs(self, digits, depth, path, result):
        if len(digits) == depth:
            result.append(path)
            # print(f"return result:{result} path:{path}")
            return
        else:
            # print("else")
            letters =  self.digitsToLetter[digits[depth]]
            # print(f"current digit:{digits[depth]}, current letters:{letters}")

            for i in range(len(letters)):
                self.bfs(digits, depth+1, path+letters[i], result)
            pass

# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    output = sol.letterCombinations("23")
    # output = sol.letterCombinations("")
    print(output)

