# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[0]
        def helper(root,m):
            if not root:return 
            if root.val>=m:
                res[0]+=1
                m=root.val
            helper(root.left,m)
            helper(root.right,m)
        helper(root,float("-inf"))
        return res[0]