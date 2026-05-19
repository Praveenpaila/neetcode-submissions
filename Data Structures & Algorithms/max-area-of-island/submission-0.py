class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(grid,i,j,nei,m,n,visited):
            res=0
            q=deque()
            q.append((i,j))
            visited.add((i,j))
            while q:
                i,j=q.popleft()
                res+=1
                for ni,nj in nei:
                    r,c=i+ni,j+nj
                    if r>=0 and r<m and c>=0 and c<n and (r,c) not in visited and grid[r][c]==1:
                        visited.add((r,c))
                        q.append((r,c))
            return res
            
        nei=[(-1,0),(1,0),(0,1),(0,-1)]
        m=len(grid)
        n=len(grid[0])
        res=0
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited :
                    res=max(res, bfs(grid,i,j,nei,m,n,visited))
        return res