class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        n = len(temperatures)
        out = n *[0]
        stack = []

        for i , t in enumerate(temperatures):
            while stack and temperatures[i] > stack[-1][1]:
                idx, temp = stack.pop() 
                out[idx] = i - idx
            stack.append([i,t])

        return out