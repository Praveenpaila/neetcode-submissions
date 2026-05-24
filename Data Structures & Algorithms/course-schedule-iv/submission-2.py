class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=[[] for i in range(numCourses)]
        indegree=[0]*numCourses
        if not prerequisites:
            return [False]*len(queries)
        for i,j in prerequisites:
            graph[i].append(j)
        res=[]
        def dfs(i,j,graph,visited):
            if i==j:return True
            visited.add((i))
            for n in graph[i]:
                if n not in visited:
                    if dfs(n,j,graph,visited):
                        return True
            return False
        for i,j in queries:
            res.append( dfs(i,j,graph,set()))
        return res