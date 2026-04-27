import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #math.sqrt(9)

        minheap = []

        res = []
        list2 = points
        idx = []

        for point in points:
            # find Euclidean distance

            x = (point[0] - 0)  ** 2
            y = (point[1] - 0)  ** 2

            ed = math.sqrt(x+y)

            heapq.heappush(minheap,ed)
            idx.append(ed)

        for i in range(k):
            mind = heapq.heappop(minheap)
            index = idx.index(mind)
            res.append(list2[index])
            idx.pop(index)
            list2.pop(index)

        
        return res










        