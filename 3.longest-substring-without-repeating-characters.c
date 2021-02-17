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

    for (int start = 0; start < length; start++) {
        for (int end = start; end < length; end++) {
            int currentlen = 0;
            char ascii[128] = {0};
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

