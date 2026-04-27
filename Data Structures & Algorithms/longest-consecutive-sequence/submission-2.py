class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()

        print(nums)

        if not nums:
            return 0

        c = 1
        m =1

        for i in range(1,len(nums)):
            print(nums[i])
            if nums[i-1] +1 == nums[i]:
                c +=1
            elif  nums[i-1] == nums[i]:
                print( nums[i-1],  nums[i])
                c = c
            else:
                c = 1
            m = max(m,c)
            print("values m ",m,"c",c)



        return m
        