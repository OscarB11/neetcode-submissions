import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        minheap = []

        res = []
       
        for point in points:
            # find Euclidean distance

            x = (point[0] - 0)  ** 2
            y = (point[1] - 0)  ** 2

            ed = math.sqrt(x+y)
            entry = [ed,point[0],point[1]]

            heapq.heappush(minheap,entry)
            

        for i in range(k):
            ed,x,y = heapq.heappop(minheap)
            
            res.append([x,y])
           
        
        return res










        