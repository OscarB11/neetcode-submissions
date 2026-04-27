class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            # if temp[i] > top of stack --> while true pop top of the stack calaculate time then add to the res 
            

            while stack and stack[-1][0] < temperatures[i]:
                item = stack.pop()
                val = item[0]
                ind = item[1]

                res[ind] = i - ind




            stack.append([temperatures[i],i])

        return res 


           


        