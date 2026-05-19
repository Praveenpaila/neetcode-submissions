class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def bfs(visited,grid,nei,i,j,m,n):
            q=[(i,j)]
            visited[i][j]=1
            while q:
                i,j=q.pop(0)
                for ni,nj in nei:
                    r,c=ni+i,nj+j
                    if r>=0 and r<m and c>=0 and c<n and visited[r][c]==0 and grid[r][c]=='1':
                        visited[r][c]=1
                        q.append((r,c))
        m=len(grid)
        n=len(grid[0])
        visited=[[0]*n for i in range(m)]
        nei=[(-1,0),(1,0),(0,1),(0,-1)]
        c=0
        for i in range(m):
            for j in range(n):
                if visited[i][j]==0 and grid[i][j]=='1':
                    bfs(visited,grid,nei,i,j,m,n)
                    c+=1
        return c
        