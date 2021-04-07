/*
 * @lc app=leetcode id=100 lang=cpp
 *
 * [100] Same Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#define DEBUG 0
#if DEBUG
#include <iostream>
#include <stdio.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
#endif

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if ((p == NULL && q != NULL) || (p != NULL && q == NULL))
            return false;

        if (p == NULL && q == NULL)
            return true;

        if (p->val == q->val) {
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
        else {
            return false;
        }
    }
};
// @lc code=end


#ifdef DEBUG
//   1      1
//  / \    / \
// 2   3  2   3
// Input: p = [1,2,3], q = [1,2,3]
// Output: true

//   1      1
//  /        \
// 2          2
// Input: p = [1,2], q = [1,null,2]
// Output: false

//   1      1
//  / \    / \
// 2   1  1   2
// Input: p = [1,2,1], q = [1,1,2]
// Output: false

int main() {
    cout << "start" << endl;
    TreeNode* a1 = new TreeNode(1);
    TreeNode* a2 = new TreeNode(2);
    TreeNode* a3 = new TreeNode(3);
    a1->left = a2;
    a1->right = a3;

    TreeNode* b1 = new TreeNode(1);
    TreeNode* b2 = new TreeNode(2);
    TreeNode* b3 = new TreeNode(0);
    b1->left = b2;
    b1->right = b3;

    Solution sol;
    sol.isSameTree(a1, b1);

    cout << sol.isSameTree(a1, b1) << endl;
    // cout << a1->val << endl;
    // cout << a1->left->val << endl;
    // cout << a1->right->val << endl;
    cout << "end" << endl;
    return 0;
}
#endif

// 2021/04/07
// Accepted
// 60/60 cases passed (0 ms)
// Your runtime beats 100 % of cpp submissions
// Your memory usage beats 99.7 % of cpp submissions (9.8 MB)