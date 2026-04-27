class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {')':'(','}':'{',']':'['}
        stack = []

        print(pairs.values()) #open
        print(pairs.keys()) #close

    

        for i in s:
            print(i,stack)
            if i in pairs.values():
                stack.append(i)
            
            elif i in pairs.keys():
                if not stack:
                    return False
                elif pairs.get(i) == stack[-1]:
                    stack.pop()
                else:
                    return False
                    

            
        
        return not stack