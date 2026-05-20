class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        out = []
        path = []
        nums.sort()

        def dfs(path,ind):
            out.append(path[:])

            for i in range(ind,len(nums)):
                if nums[i] == nums[i-1] and i > ind:
                    continue
                path.append(nums[i])
                dfs(path,i+1)
                path.pop()
        
        dfs(path,0)
        return out