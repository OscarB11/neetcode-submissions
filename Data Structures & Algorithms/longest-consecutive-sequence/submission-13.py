class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        numset = set(nums)
        res = 0
        count = 1
        print(numset)

        for i in numset:
            while i + count in numset:
                count +=1
            
            
            res = max(res,count)
            count =1
       
        return res
