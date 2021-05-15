/*
 * @lc app=leetcode id=145 lang=cpp
 *
 * [145] Binary Tree Postorder Traversal
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
class Solution {
public:
    vector<int> result;

    vector<int> postorderTraversal(TreeNode* root) {
        postorder(root);
        return result;
    }

    void postorder(TreeNode* node) {
        if (!node) {
            return;
        }
        postorder(node->left);
        postorder(node->right);
        result.push_back(node->val);
        // cout << node->val << endl;
    }
};
// @lc code=end

