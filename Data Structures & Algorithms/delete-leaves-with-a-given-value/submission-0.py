# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: int
        :rtype: Optional[TreeNode]
        """
        def rem(root,target):
            if not root:return
            root.left=rem(root.left,target)
            root.right=rem(root.right,target)
            if not root.left and not root.right and root.val==target:
                return 
            return root
        return rem(root,target)
