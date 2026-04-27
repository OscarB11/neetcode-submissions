class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        out = 0 
        stack = []
        ops = ['+', '-', '*', '/']
       
        for i in tokens:
            print(i)
            print(stack)
            if i not in ops:
                stack.append(int(i))
            elif i in ops:
                v1 = stack.pop()
                v2 = stack.pop()
                expression = f"{v2} {i} {v1}"
                result = eval(expression)
                result = int(result)
                stack.append(result)

        
        return stack[-1]

        