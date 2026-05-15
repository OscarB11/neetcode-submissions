import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]



        if len(stones) == 1:
            return stones[0]
        
        heapq.heapify(maxheap)
        
        print(maxheap)
        while len(maxheap) >1:
            v1 = -heapq.heappop(maxheap)
            v2 = -heapq.heappop(maxheap)
            print(v1,v2,maxheap)

            new = abs(v1-v2)
            if new == 0:
                continue
            else:
                heapq.heappush(maxheap,-new)
            print(v1,v2,maxheap)
        
        return -maxheap[0] if maxheap else  0


