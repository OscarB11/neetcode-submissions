class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        out = n * [0]

        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT , stackI = stack.pop()
                out[stackI] = (i - stackI)
            stack.append([t,i])


        return out
        