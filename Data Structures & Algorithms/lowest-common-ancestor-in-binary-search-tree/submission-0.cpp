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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // If p and q > curr, go right
        if (p->val >= root->val && 
            q->val >= root->val) {
            if (root->val == q->val || root->val == p->val)
            {
                return root;
            }
            if (root->right != nullptr) {
                return lowestCommonAncestor(root->right, p, q);
            }
        }
        // if p and q < curr, go left
        if (p->val <= root->val && 
            q->val <= root->val) {
            cout << "hello";
            if (root->val == q->val || root->val == p->val)
            {
                return root;
            }
            if (root->left != nullptr) {
                return lowestCommonAncestor(root->left, p, q);
            }
        }
        cout << "hello";
        return root;
    }
};
