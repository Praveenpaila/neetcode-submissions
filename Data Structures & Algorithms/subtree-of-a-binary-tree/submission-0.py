# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def same(a,b):
            if not a and not b:return True
            if not a or not b:return False
            if a.val!=b.val:return False
            return same(a.left,b.left) and same(a.right,b.right)
        def helper(root,subRoot):
            if not root:return False
            if root.val==subRoot.val and same(root,subRoot):return True

            
            return helper(root.left,subRoot) or helper(root.right,subRoot)
            
        return helper(root,subRoot)