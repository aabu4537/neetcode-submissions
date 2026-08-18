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

        let post = [];
        this.helper(root, post);
        return post;
            
    }

    helper(node, post){
        if (!node){
            return;
        }
        this.helper(node.left, post);
        this.helper(node.right, post);
        post.push(node.val);
    }
}
