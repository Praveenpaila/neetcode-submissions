class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res=0

        left=[0]*len(height)
        left[0]=height[0]
        for i in range(len(height)):
            left[i]=max(left[i-1],height[i])
        right=[0]*len(height)
        right[-1]=height[-1]
        for i in range(len(height)-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        for i in range(1,len(height)-1):
            l,r=left[i],right[i]
            water=min(l,r)-height[i]
            if water>0:
                res+=water
        return res
        