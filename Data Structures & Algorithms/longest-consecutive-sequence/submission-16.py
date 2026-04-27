class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = sorted(nums)
        print(snums)
        if len(nums) ==1:
            return 1
        elif nums == []:
            return 0

        res = 0
        count =0


        for i in range(len(snums)-1):
            if snums[i]+1 == snums[i+1]:
                count +=1
                res = max(res,count)
            elif snums[i] == snums[i+1]:
                count = count
            else:
                count = 0 
            res = max(res,count)


            


        return res+1
        