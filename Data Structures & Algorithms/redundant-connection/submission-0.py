class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n=len(edges)
        parent=[i for i in range(0,n+1)]
        size=[1]*(n+1)
        def find(a):
            if parent[a]==a:
                return a
            parent[a]=find(parent[a])
            return parent[a]

        def union(a,b):
            ua=find(a)
            ub=find(b)
            if ua==ub:
                return True
            else:
                parent[ua]=ub
                size[ub]+=size[ua]
                return False
        i,j=0,0
        for i,j in edges:
            if union(i,j):
                return [i,j]
        return [i,j]