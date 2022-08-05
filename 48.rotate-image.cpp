/*
 * @lc app=leetcode id=48 lang=cpp
 *
 * [48] Rotate Image
 */

// https://www.cnblogs.com/grandyang/p/4389572.html
// http://glj8989332.blogspot.com/2019/09/leetcode-48-rotate-image.html

#define DEBUG 0
#ifdef DEBUG
#include <iostream>
#include <vector>
using namespace std;
#endif

// @lc code=start
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        vector<vector<int>> rotate_matrix = matrix;

        int n = matrix.size() -1;
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                rotate_matrix[i][j] = matrix[n-j][i];
            }
        }
        matrix = rotate_matrix;
    }
};
// @lc code=end

#ifdef DEBUG
int main() {
    printf("start\n");
    vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    printf("matrix size:%d\n", matrix[0].size());

    for (int i = 0; i < matrix.size() ; i++) {

        for (int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;

    Solution sol;
    sol.rotate(matrix);

    for (int i = 0; i < matrix.size(); i++) {

        for (int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    printf("end\n");
    return 0;
}
#endif