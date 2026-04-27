class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        top =0 
        bot = row -1

        while top <= bot:

            midrow = (top+bot)//2

            if target > matrix[midrow][-1]:
                top = midrow+1
            elif target < matrix[midrow][0]:
                bot = midrow-1
            else:
                break
        
       
        

        midrow = (top+bot)//2

        l = 0
        r = col-1

        while l <= r:
            m = (l+r)//2
            if target > matrix[midrow][m]:
                l = m+1
            elif target< matrix[midrow][m]:
                r = m-1
            else:
                return True
        
        return False 


        