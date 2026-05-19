# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:return []
        hash={}
        q=deque([(root,0)])
        while q:
            root,val=q.popleft()
            if val in hash:
                hash[val].append(root.val)
            else:
                hash[val]=[root.val]
            if root.left:
                q.append((root.left,val+1))
            if root.right:
                q.append((root.right,val+1))
        return list(hash.values())
        return []