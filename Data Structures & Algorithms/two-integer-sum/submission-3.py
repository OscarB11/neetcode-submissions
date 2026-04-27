class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []

        for i in range(len(nums)):
            print(target - nums[i])
            if (target - nums[i] ) in seen:
                pos =  nums.index(target - nums[i]) 
                return [pos,i]
            else:
                seen.append(nums[i])
            