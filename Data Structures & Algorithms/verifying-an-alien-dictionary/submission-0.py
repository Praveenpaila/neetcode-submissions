class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(len(words)-1):
            f=len(words[i])
            s=len(words[i+1])
            fc=0
            sc=0
            while fc<f and sc<s and words[i][fc]==words[i+1][sc]:
                fc+=1
                sc+=1
            if fc==f :continue
            if sc==s:return False
            a=words[i][fc]
            b=words[i+1][sc]
            flag=0
            for j in order:
                if j==a:
                    flag=1
                if j==b:
                    if flag==0:
                        return False
                    break
        return True