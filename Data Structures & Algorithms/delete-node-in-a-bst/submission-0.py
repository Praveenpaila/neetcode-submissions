# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        def successor(root):
            node=root.right
            while node.left:
                node=node.left
            return node.val
        def dele(root,key):
            if not root:return 
            if key<root.val:
                root.left=dele(root.left,key)
            elif key>root.val:
                root.right=dele(root.right,key)
            else:
                if not root.left and not root.right:return 
                if not root.left:return root.right
                if not root.right:return root.left
                s=successor(root)
                root.val=s
                root.right=dele(root.right,s)

            return root
        return dele(root,key)
            