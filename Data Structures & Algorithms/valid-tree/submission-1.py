class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        rank=[1]*n
        par=[i for i in range(n)]
        def findParent(a):
            if par[a]==a:return par[a]
            par[a]=findParent(par[a])
            return par[a]
        def union(a,b):
            a=findParent(a)
            b=findParent(b)
            if a==b:
                return False
            if rank[a]>rank[b]:
                par[b]=a
                rank[a]+=rank[b]
            else:
                par[a]=b
                rank[b]+=rank[a]
            return True
        for i,j in edges:
            if not union(i,j):return False
        if len(edges) != n-1:return False
        return True
        