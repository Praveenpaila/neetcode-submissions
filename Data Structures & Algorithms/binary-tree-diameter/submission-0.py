# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:return -1
            return 1+max(height(root.left),height(root.right))
        def helper(root):
            if not root or (not root.left and not root.right):return 0
            if not root.left:
                return height(root.right)+1
            if not root.right:
                return height(root.left)+1
            return height(root.left)+height(root.right)+2
        ans=[0]
        def pre(root):
            if not root:return
            ans[0]=max(ans[0],helper(root))
            pre(root.left)
            pre(root.right)
        pre(root)
        return ans[0]
