/*
 * @lc app=leetcode id=3 lang=c
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start


int lengthOfLongestSubstring(char * s){

    int length = strlen(s);
    int maxlen = 0;

    for (int i = 0; i < length; i++) {
        bool ascii[128] = {0};

        for (int j = i; j < length; j++) {
            if (ascii[s[j]] == 0) {
                ascii[s[j]] = 1;
                maxlen = fmax(maxlen, j - i + 1);
                // printf("i:%d, j:%d, maxlen:%d\n", i, j, maxlen);
            }
            else {
                break;
            }
        }
    }

    return maxlen;
}
// @lc code=end

