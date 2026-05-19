class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):return False
        window=s2[:len(s1)]
        s1=sorted(s1)
        if sorted(window)==s1:return True
        for i in range(len(window),len(s2)):
            window=window[1:]
            window+=s2[i]
            if sorted(window)==s1:return True
        return False
    