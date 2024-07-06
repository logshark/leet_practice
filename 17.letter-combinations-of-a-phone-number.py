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

    def letterCombinations(self, digits: str) -> List[str]:
        digitsToLetter = {'2': ['a','b','c'], '3': ['d','e','f'] , '4': ['g','h','i'] , '5': ['j','k','l'] ,
                        '6': ['m','n','o'], '7': ['p','q','r', 's'], '8': ['t','u','v'] , '9': ['w','x','y', 'z']}


        if len(digits) == 0:
            return []

        result = [""]

        for i in digits:
            print(f"digits:{i}")
            tmp = []
            for s in result:
                print(f"result{s}")
                for c in digitsToLetter[i]:
                    # print(c)
                    tmp.append(s+c)
                    print(f"tmp:{tmp}")

            result = tmp



        return result

# @lc code=end


# https://zxi.mytechroad.com/blog/searching/leetcode-17-letter-combinations-of-a-phone-number/
if __name__ == '__main__':
    sol = Solution()
    output = sol.letterCombinations("23")
    # output = sol.letterCombinations("")
    print(output)

