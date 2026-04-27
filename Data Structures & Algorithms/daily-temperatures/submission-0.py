class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)

        for i in range(length):
            print(temperatures[i])
            count = 0
            stack.append(0)
            for x in range(i,length):
                if temperatures[x] > temperatures[i]:
                    stack[i]=count
                    break
                else:
                    count += 1 
                print("after",temperatures[x] )
            
            
        
        return stack