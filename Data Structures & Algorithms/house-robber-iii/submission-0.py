# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        dp={}

        def fun(root):
            if not root:return 0
            if root  in dp:
                return dp[root]

            dp[root]= max(fun(root.left)+fun(root.right),root.val+fun(root.left.left if root.left else None)+fun(root.left.right if root.left else None)+fun(root.right.left if root.right else None)+fun(root.right.right if root.right else None))
            return dp[root]
        return fun(root)