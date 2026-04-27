class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        out = []

        def generate(opennum, closednum):

            if opennum == closednum == n:
                out.append("".join(stack))
                return   
            
            if opennum < n:
                stack.append("(")
                generate(opennum+1,closednum) 
                stack.pop()
        
            if closednum < opennum:
                stack.append(")")
                generate(opennum,closednum+1) 
                stack.pop()
        
        
        generate(0,0)
        return out