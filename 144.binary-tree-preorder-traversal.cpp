/*
 * @lc app=leetcode id=144 lang=cpp
 *
 * [144] Binary Tree Preorder Traversal
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
// #include "struct.h"

class Solution {
public:
    vector<int> result;

    vector<int> preorderTraversal(TreeNode* root) {
        preorder(root);
        return result;
    }

    void preorder(TreeNode* node) {
        if (!node) {
            return;
        }
        result.push_back(node->val);
        // cout << node->val << endl;
        preorder(node->left);
        preorder(node->right);
    }
};
// @lc code=end

#ifdef DEBUG
int main() {
    printf("start\n");
    TreeNode *t1 = new TreeNode(1);
    TreeNode *t2 = new TreeNode(2);
    TreeNode *t3 = new TreeNode(3);
    t1->right = t2;
    t2->left = t3;

    Solution sol;
    vector<int> result = sol.preorderTraversal(t1);

    cout << "result" << endl;
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << endl;
    }
    printf("end\n");
}
#endif