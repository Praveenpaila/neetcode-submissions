class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def bfs(grid,i,j,nei,m,n,visited):
            res=0
            q=deque()
            q.append((i,j))
            visited.add((i,j))
            flag=1
            mark=[]
            while q:
                i,j=q.popleft()
                if i==0 or j==0 or i==m-1 or j==n-1:flag=0
                mark.append([i,j])
                for ni,nj in nei:
                    r,c=i+ni,j+nj
                    if r>=0 and r<m and c>=0 and c<n and (r,c) not in visited and grid[r][c]=='O':
                        visited.add((r,c))
                        q.append((r,c))
                        
            if flag:
                for i,j in mark:
                    grid[i][j]='X'

        nei=[(-1,0),(1,0),(0,1),(0,-1)]
        m=len(board)
        n=len(board[0])
        visited=set()
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and (i,j) not in visited:
                    bfs(board,i,j,nei,m,n,visited)