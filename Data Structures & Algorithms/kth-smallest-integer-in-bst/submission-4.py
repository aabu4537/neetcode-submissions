# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        
        arr = []
        def Helper(a):
            if not a:
                return
            Helper(a.left)
            arr.append(a.val)
            Helper(a.right)
        Helper(root)
        return arr[k-1]