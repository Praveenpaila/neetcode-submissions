# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(a,b):
            if not a and not b:return True
            if not a or not b:return False
            if a.val!=b.val:return False
            return same(a.left,b.left) and same(a.right,b.right)
        return same(p,q)