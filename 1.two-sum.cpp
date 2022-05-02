/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

#define DEBUG 0

#if DEBUG
#include <iostream>
#include <vector>
using namespace std;
using std::vector;
#endif

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        vector<int> ans;

        if (nums.size() < 2)
            return ans;

        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j < nums.size(); j++) {

                if (nums[i] + nums[j] == target)
                {
                    ans.push_back(i);
                    ans.push_back(j);
                    return ans;
                }
            }
        }

        return ans;
    }
};
// @lc code=end

#if DEBUG
int main(){

    vector<int> nums;

    nums.push_back(2);
    nums.push_back(7);
    nums.push_back(11);
    nums.push_back(15);

    int target = 9;

    Solution sol;
    vector<int> result = sol.twoSum(nums, target);

    vector<int>::iterator result_intr = result.begin();

    for (vector<int>::iterator it = result.begin(); it != result.end(); it++) {
       cout << *it << "\n";
    }

    return 0;
}
#endif