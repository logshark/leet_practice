/*
 * @lc app=leetcode id=66 lang=cpp
 *
 * [66] Plus One
 */

#define DEBUG 0
#ifdef DEBUG
#include <iostream>
#include <vector>
using namespace std;
#endif

// @lc code=start
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        int end = digits.size() - 1;
        digits[end] += 1;

        for(int i = end; i >= 0; i--)
        {
            if (digits[i] == 10) {
                digits[i] = 0;
                if (i == 0) {
                    digits.insert(digits.begin(), 1);
                } else {
                    digits[i-1] += 1;
                }

            }
        }

        return digits;
    }
};
// @lc code=end


#ifdef DEBUG
int main() {

    vector<int> digits = {9, 9, 9};
    printf("end:%d\n", digits[digits.size() -1]);

    Solution sol;
    digits = sol.plusOne(digits);
    for (int i = 0; i < digits.size(); i++) {
        printf("%d ", digits[i]);
    }
    printf("\n");

}
#endif