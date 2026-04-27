class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
       
        ops = ['+', '-', '*', '/']

        for i in tokens:
            print(stack)
            if i in ops:
                x = stack.pop()
                y = stack.pop()
                if i == "+":
                    stack.append(x+y)
                elif i == "-":
                    stack.append(y-x)
                elif i == "*":
                    stack.append(y*x)
                else:
                    stack.append(int(y / x))

            else:
                stack.append(int(i))
        
        print(stack)

        return stack[-1] 

        
    
        