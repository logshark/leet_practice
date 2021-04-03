/*
 * @lc app=leetcode id=48 lang=cpp
 *
 * [48] Rotate Image
 */

#include <iostream>
#include <vector>
using namespace std;

void swap(int &a, int &b) {
    a ^= b;
    b ^= a;
    a ^= b;
}


// @lc code=start
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[i].size(); j++) {

                int tmp = matrix[i][j];


            }
            cout << endl;
        }
        cout << endl;
    }
};
// @lc code=end

// https://www.cnblogs.com/grandyang/p/4389572.html
// http://glj8989332.blogspot.com/2019/09/leetcode-48-rotate-image.html

int main() {
    printf("start\n");

    int a = 2;
    int b = 3;

    swap(a, b);
    printf("a:%d b:%d\n", a, b);

    vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    printf("matrix size:%d\n", matrix.size());

    for (int i = 0; i < matrix.size() -1 ; i++) {

        for (int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
    printf("111\n");

    Solution sol;
    sol.rotate(matrix);

    printf("end\n");
    return 0;
}