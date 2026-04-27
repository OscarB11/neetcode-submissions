class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        new = []
        for pair in count:
            inp = (count[pair],pair)
            new.append(inp)

        new.sort()
        new.reverse()
        result =[]

        for i in range(k):
            result.append(new[i][1])
        return result













