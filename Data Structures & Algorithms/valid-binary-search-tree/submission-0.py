# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        q=[(root,float("-inf"),float("inf"))]
        while q:
            root,l,r=q.pop(0)
            if not root:
                continue
            if root.val<=l or root.val>=r:
                return False
            if root.left:
                if (root.val<=root.left.val):return False
                q.append((root.left,l,root.val))
            if root.right:
                if (root.val>=root.right.val) :return False
                q.append((root.right,root.val,r))
        return True