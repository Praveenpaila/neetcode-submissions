class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for i in asteroids:
            while stack and i<0 and stack[-1]>0:
                if stack[-1]<-i:
                    stack.pop()
                    continue
                elif stack[-1]==-i:
                    stack.pop()
                break
            else:
                stack.append(i)
        return stack