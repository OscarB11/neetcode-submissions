class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0 

          #start >= prevend

        prevend = float('-inf')

        for start,end in intervals:
            if start >= prevend:
                prevend = end
            else:
                res +=1
                prevend = min(prevend,end)
        
        return res
        
