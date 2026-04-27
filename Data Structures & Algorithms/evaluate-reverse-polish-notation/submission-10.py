class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                v2, v1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(v1 + v2)
                elif token == '-':
                    stack.append(v1 - v2)
                elif token == '*':
                    stack.append(v1 * v2)
                elif token == '/':
                    stack.append(int(float(v1) / float(v2)))  # Integer division truncates towards zero

        return stack[-1]

        