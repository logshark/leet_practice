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
        print(s)
        # print(f"len:{len(s)}")

        # last index of every character
        lastIdx = {}
        max_len = 0

        # starting index of current
        # window to calculate max_len
        startIdx = 0

        for i in range(0, len(s)):
            print(f"loop:{i} s:{s[i]}")
            # Find the last index of str[i]
            # Update startIdx (starting index of current window)
            # as maximum of current value of startIdx and last index plus 1
            if s[i] in lastIdx:
                print(f"    startIdx:{startIdx}, lastIdx[s[i]]+1:{lastIdx[s[i]] + 1}")
                startIdx = max(startIdx, lastIdx[s[i]] + 1)
                print(f"    update startIdx:{startIdx}")
                

            # Update result if we get a larger window
            max_len = max(max_len, i-startIdx + 1)

            # Update last index of current char.
            lastIdx[s[i]] = i

            print(f"    maxLen:{max_len} startIdx:{startIdx} lastIdx:{lastIdx}")

        return max_len

# @lc code=end

# https://www.geeksforgeeks.org/python-program-to-find-length-of-the-longest-substring-without-repeating-characters/?ref=ml_lbp
# https://hackmd.io/@meyr543/Sk99l4OjY
if __name__ == '__main__':
    sol = Solution()
    # output = sol.lengthOfLongestSubstring("pwwkew")
    output = sol.lengthOfLongestSubstring("abba")
    # output = Solution.lengthOfLongestSubstring(Solution, "pwwkew")
    print(output)
