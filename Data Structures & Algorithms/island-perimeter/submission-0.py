class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(grid,i,j,nei,m,n):
            res=0
            q=deque()
            q.append((i,j))
            visited=set()
            visited.add((i,j))
            while q:
                i,j=q.popleft()
                if i==0:
                    res+=1
                if j==0:
                    res+=1
                if i==m-1:
                    res+=1
                if j==n-1:
                    res+=1
                if j-1>=0 and grid[i][j-1]==0:
                    res+=1
                if j+1<n and grid[i][j+1]==0:
                    res+=1
                if i+1<m and grid[i+1][j]==0:res+=1
                if i-1>=0 and grid[i-1][j]==0:res+=1

                for ni,nj in nei:
                    r,c=i+ni,j+nj
                    if r>=0 and r<m and c>=0 and c<n and (r,c) not in visited and grid[r][c]==1:
                        visited.add((r,c))
                        q.append((r,c))
            return res
            
        nei=[(-1,0),(1,0),(0,1),(0,-1)]
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return bfs(grid,i,j,nei,m,n)