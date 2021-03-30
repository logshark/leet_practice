/*
 * @lc app=leetcode id=7 lang=cpp
 *
 * [7] Reverse Integer
 */

// @lc code=start

#define DEBUG 0
#if DEBUG
#include <stdio.h>
#include <limits.h>
#include <iostream>

using namespace std;
#endif

class Solution {
public:
    int reverse(int x) {

        if (x == 0) {
            return 0;
        }
        
        int reverse_x = 0;

        while (x != 0) {
            if (reverse_x > 0 && reverse_x > (INT_MAX / 10))
                return 0;
            if (reverse_x < 0 && reverse_x < (INT_MIN / 10))
                return 0;
            reverse_x = reverse_x * 10;
            reverse_x += x % 10;
            x = x / 10;
        }
        
        return reverse_x;
    }
};
// @lc code=end

#if DEBUG
int main(int argc, char* argv[])
{
    cout << INT_MAX << endl;
    cout << INT_MIN << endl;
    Solution sol;
    printf("result: %d\n", sol.reverse(-123));
    printf("end\n");
    return 0;
}
#endif