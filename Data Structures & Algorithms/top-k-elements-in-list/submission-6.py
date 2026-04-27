class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)

        #print(freq)
        asort = []
        for i in freq:
            val = i
            count = freq[i]
            item = [count,val]
            asort.append(item)

        #print(asort)
        asort2 = sorted(asort,reverse = True)
        #print(asort2)
        
        output = []

        for i in range(k):
            res = asort2[i][1]
            output.append(res)


               
        return output