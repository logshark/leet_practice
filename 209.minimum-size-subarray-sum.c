/*
 * @lc app=leetcode id=209 lang=c
 *
 * [209] Minimum Size Subarray Sum
 */

// @lc code=start
#include <limits.h>

int minSubArrayLen(int target, int* nums, int numsSize){
    int result = INT_MAX;
    int start = 0;
    int currentSum = 0;
    
    for (int end = 0; end < numsSize; end++) {
        currentSum += nums[end];
         while (currentSum >= target) {
            if ((end - start + 1) < result)
                result = (end - start + 1);
            currentSum -= nums[start];
            start += 1;
        }
    }
    
    return result == INT_MAX ? 0: result ;
}
// @lc code=end

