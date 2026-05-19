class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(grid,visited,q,m,n,nei):
            t=0
            while q:
                i,j,t=q.popleft()
                for ni,nj in nei:
                    r=i+ni
                    c=j+nj
                    if r>=0 and r<m and c>=0 and c<n and visited[r][c]==0 and grid[r][c]==1:
                        visited[r][c]=1
                        q.append((r,c,t+1))
            return t
        
        m=len(grid)
        n=len(grid[0])
        nei=[(-1,0),(1,0),(0,-1),(0,1)]
        visited=[[0]*n for i in range(m)]
        c=0
        q=deque()
        for i in range(m):
            for j in range(n):
                if  grid[i][j]==2:
                    visited[i][j]=1
                    q.append((i,j,0))
        c=bfs(grid,visited,q,m,n,nei)
        for i in range(m):
            for j in range(n):
                if  grid[i][j]==1 and not visited[i][j]:
                    return -1
                    
        
        
        return c
      

        