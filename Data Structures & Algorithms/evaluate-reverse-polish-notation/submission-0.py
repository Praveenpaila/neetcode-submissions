class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        
        for t in tokens:
            if t in "+-*/":
                a = stack.pop()
                b = stack.pop()
                
                if t == '+':
                    stack.append(b + a)
                elif t == '-':
                    stack.append(b - a)
                elif t == '*':
                    stack.append(b * a)
                else:
                    c=b//a
                    if c<0 and b%a!=0:
                        c+=1
                    stack.append(c) 
            else:
                stack.append(int(t))
        
        return stack[-1]