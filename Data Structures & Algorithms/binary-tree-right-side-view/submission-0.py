# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:return []
        res=[]
        q=deque([(root,0)])
        while q:
            root,r=q.popleft()
            if r<len(res):
                res[r]=root.val
            else:
                res.append(root.val)
            if root.left:
                q.append((root.left,r+1))
            if root.right:
                q.append((root.right,r+1))
        return res