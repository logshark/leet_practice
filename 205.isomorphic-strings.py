#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s = dict()
        dict_t = dict()

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in dict_s:
                if dict_s.get(char_s) == dict_t.get(char_t):
                    dict_s[char_s] = i
                    dict_t[char_t] = i
                else:
                    # print("False1")
                    return False
            else:
                if char_t in dict_t:
                    # print("False2")
                    return False
                else:
                    dict_s[char_s] = i
                    dict_t[char_t] = i

            # print(dict_s)
            # print(dict_t)

        print("True")
        return True

# @lc code=end

