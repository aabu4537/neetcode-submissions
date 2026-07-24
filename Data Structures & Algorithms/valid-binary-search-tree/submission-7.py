# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def Helper(a, left, right):
            if not a:
                return True
            if a.val <= left or a.val >= right:
                return False
            return Helper(a.left, left, a.val) and Helper(a.right, a.val, right)

        
        return Helper(root, -float("inf"), float("inf"))
        