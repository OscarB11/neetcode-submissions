class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        def dfs(curr):
            if len(curr) == len(nums):
                out.append(curr[:])
                return 
            
            for i in nums:
                if i not in curr:
                    
                    curr.append(i)
                    #print(i,curr)
                    dfs(curr)
                    curr.pop ()

        dfs([])
        return out