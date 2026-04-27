class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # def __init__(self, k, nums):
        #     self.k = k
        #     self.heap = nums
        #     heapq.heapify(self.heap)
        #     while len(self.heap) > k:
        #         heapq.heappop(self.heap)

        # def add(self, val):
        #     heapq.heappush(self.heap, val)
        #     if len(self.heap) > self.k:
        #         heapq.heappop(self.heap)
        #     return self.heap[0]



        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        print(maxheap)
        

        while len(maxheap) > 1:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)

            if x ==y:
               continue
            elif x < y:
                print(x,y,y-x)
                new = (y -x)
                heapq.heappush(maxheap,-new)
            else:
                print(x,y,x-y)
                new2 = (x -y)
                heapq.heappush(maxheap,-new2)

        if maxheap:
            return -maxheap[0]
        else:
            return 0



        