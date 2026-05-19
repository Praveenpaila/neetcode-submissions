class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def getStates(states):
            res=[]
            # print(type(states))
            for i in range(4):
                res.append(states[:i]+str((int(states[i])+1)%10)+states[i+1:])
                res.append(states[:i]+str((int(states[i])-1)%10)+states[i+1:])
            return res
        if '0000' in deadends:return -1
        q=[('0000',0)]
        deadends=set(deadends)
        deadends.add('0000')
        
        while q:
             state,count=q.pop(0)
             if state==target:return count
             for i in getStates(state):
                if i not in deadends:
                    deadends.add(i)
                    q.append((i,count+1))
        return -1