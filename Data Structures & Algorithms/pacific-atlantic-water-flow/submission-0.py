from collections import deque

class Solution(object):
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                i, j = q.popleft()
                for di, dj in dirs:
                    r, c = i+di, j+dj
                    if 0<=r<m and 0<=c<n and (r,c) not in visited \
                            and heights[r][c] >= heights[i][j]:
                        visited.add((r,c))
                        q.append((r,c))
            return visited

        pacific_starts  = [(i,0) for i in range(m)] + [(0,j) for j in range(n)]
        atlantic_starts = [(i,n-1) for i in range(m)] + [(m-1,j) for j in range(n)]

        pacific  = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [[i,j] for i in range(m) for j in range(n)
                if (i,j) in pacific and (i,j) in atlantic]