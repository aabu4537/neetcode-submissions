/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[]}
     */
    postorderTraversal(root) {

        if (!root){
            return [];
        }

        let post = [];

        function helper(node){
            if (!node){
                return;
            }
            helper(node.left);
            helper(node.right);
            post.push(node.val);
        }

        helper(root);
        return post;
    }
}
