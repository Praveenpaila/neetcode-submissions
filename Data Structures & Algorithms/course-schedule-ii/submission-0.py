class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        graph=[[] for i in range(numCourses)]
        indegree=[0]*numCourses
        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i]+=1
        q=deque()
        for j,i in enumerate(indegree):
            if i==0:
                q.append(j)
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for i in graph[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        return res if len(res)==numCourses else []

        
        
            
