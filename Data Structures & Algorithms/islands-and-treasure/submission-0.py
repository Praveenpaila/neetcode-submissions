class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j,0))
                    visited.add((i,j))
        while q:
            i,j,val=q.popleft()
            grid[i][j]=val
            for ni,nj in [(-1,0),(1,0),(0,-1),(0,1)]:
                r,c=i+ni,j+nj
                if r>=0 and r<m and c>=0 and c<n and (r,c) not in visited and grid[r][c]!=-1:
                    visited.add((r,c))
                    q.append((r,c,val+1))
