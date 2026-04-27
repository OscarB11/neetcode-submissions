class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        print(maxheap)
        

        while len(maxheap) > 1:
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)

            if x ==y:
               continue
            elif x < y:
                new =abs (y -x)
                heapq.heappush(maxheap,-new)
            else:
                new2 = abs(x -y)
                heapq.heappush(maxheap,-new2)

        if maxheap:
            return -maxheap[0]
        else:
            return 0



        