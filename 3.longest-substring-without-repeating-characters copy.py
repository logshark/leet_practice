#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (34.87%)
# Likes:    39374
# Dislikes: 1865
# Total Accepted:    5.8M
# Total Submissions: 16.7M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # print(s)
        # print(f"len:{len(s)}")
        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                currentlen = 0
                ascii = [False for _ in range(128)]
                # print(f"i:{i} j:{j}")

                for k in range(i, j+1):
                    # print(s[k])

                    if ascii[ord(s[k])] == False:
                        ascii[ord(s[k])] = True
                        currentlen += 1
                        result = max(result, currentlen)
                        # print(f"True {currentlen}")
                    else:
                        # print("False")
                        break
                # print(" ")

        return result


# @lc code=end

if __name__ == '__main__':
    output = Solution.lengthOfLongestSubstring(Solution, " ")
    print(output)
