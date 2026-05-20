class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        c=""
        for i in strs[0]:
            c+=i
            for j in strs:
                if not(j.startswith(c)):
                    return c[:-1]
        return c
        