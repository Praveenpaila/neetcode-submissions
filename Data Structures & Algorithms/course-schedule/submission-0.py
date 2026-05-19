class Solution(object):
    def canFinish(self, numCourses, prerequisites):
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
        res=0
        while q:
            node=q.popleft()
            res+=1
            for i in graph[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        return res==numCourses

        
        
            
        