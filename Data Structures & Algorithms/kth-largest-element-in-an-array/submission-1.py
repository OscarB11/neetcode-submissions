import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        arr = nums

        heapq.heapify(arr)
        print(arr)
        while len( arr)> k:
             heapq.heappop(arr)
        print(arr)
        return arr[0]
        