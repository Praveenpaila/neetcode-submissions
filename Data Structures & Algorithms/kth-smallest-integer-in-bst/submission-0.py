# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        def find(root):
            if not root:
                return float("inf")
            if not root.left and not root.right:
                return root.val
            return min(root.val,find(root.left),find(root.right))
        def deleteNode(root, key):
            if not root:
                return None

            if key < root.val:
                root.left = deleteNode(root.left, key)

            elif key > root.val:
                root.right = deleteNode(root.right, key)

            else:  # root.val == key → delete this node

                # case 1: no child
                if not root.left and not root.right:
                    return None

                # case 2: one child
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left

                # case 3: two children
                temp = root.right
                while temp.left:
                    temp = temp.left   # inorder successor

                root.val = temp.val
                root.right = deleteNode(root.right, temp.val)

            return root


        for i in range(k):
            v=find(root)
            # c=v
            # print(v)
            root=deleteNode(root,v)
            # print(root)
        return v