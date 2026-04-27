class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {')': '(', '}':'{', ']':'['}
        stack = []

        print(pairs.keys(),"\n",pairs.values())

        for i in s:
            print(stack)
            if i in pairs.values():
                stack.append(i)
            elif i in pairs.keys():
                if stack and stack[-1] == pairs.get(i):
                    stack.pop()
                else:
                    return False

        return not stack