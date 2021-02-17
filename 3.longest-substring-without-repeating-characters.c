/*
 * @lc app=leetcode id=3 lang=c
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start


int lengthOfLongestSubstring(char * s){

    // Time Limit Exceeded 986/987 cases passed (N/A) 

    int length = strlen(s);
    int maxlen = 0;

    if (length == 1)
    {
        return length;
    }

    for (int start = 0; start < length-1; start++) {
        for (int end = start+1; end < length; end++) {
            int currentlen = 0;
            char ascii[256] = {0};
            for (int idx = start; idx <= end; idx++) {
                int current = s[idx];

                if (ascii[current] == 0) {
                    ascii[current] = 1;
                    currentlen++;
                    if (currentlen > maxlen)
                        maxlen = currentlen;
                }
                else {
                    break;
                }
            }
        }
    }

    return maxlen;
}
// @lc code=end

