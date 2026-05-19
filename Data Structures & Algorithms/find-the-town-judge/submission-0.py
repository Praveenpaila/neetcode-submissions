class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust and n==1 :return 1
        hash={}
        can=set()
        for u,v in trust:
            hash[v]=hash.get(v,0)+1
            can.add(u)
        for i,j in hash.items():
            if j==n-1 and i not in can:
                return i
            
        return -1