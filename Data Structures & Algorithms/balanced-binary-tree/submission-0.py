# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height(root):
            if not root:return -1
            return 1+max(height(root.left),height(root.right))
        def helper(root):
            if not root:return True
            left=height(root.left)
            right=height(root.right)
            if abs(left-right)>=2:return False
            return helper(root.left) and helper(root.right)
        return helper(root)