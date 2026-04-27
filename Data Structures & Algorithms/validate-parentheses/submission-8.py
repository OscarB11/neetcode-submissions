class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {')':'(','}':'{',']':'['}
        stack = []

    

        for i in s:
            print(stack)
            if i in pairs.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if top != pairs[i]:
                        return False
              
            
        
        return not stack