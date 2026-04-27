class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {')':'(','}':'{',']':'['}
        stack = []

        print(pairs.values()) #open
        print(pairs.keys()) #close


        for i in s:
            if i in pairs.values():
                stack.append(i)
            else:
                if stack and pairs.get(i) == stack[-1]:
                    stack.pop()
                else:
                    return False

           

        return not stack

    