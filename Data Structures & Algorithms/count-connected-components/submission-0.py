class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for i in range(n)]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited=set()
        c=0
        for i in range(n):
            if i not in visited:
                q=deque([i])
                visited.add(i)
                while q:
                    i=q.popleft()
                    for n in graph[i]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
                c+=1
        return c
