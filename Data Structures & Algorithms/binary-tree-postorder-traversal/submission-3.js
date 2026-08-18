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

        const stack = [root];
        const res = [];

        if(!root){
            return res;
        }

        while (stack.length > 0){
            const node = stack.pop();
            res.push(node.val);
            if (node.left){
                stack.push(node.left);
            }

            if (node.right){
                stack.push(node.right);
            }

        }

        return res.reverse();
            
    }
}
