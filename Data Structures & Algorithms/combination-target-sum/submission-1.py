class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        out = []
        path = []
        start= 0

        end = len(nums)


        def dfs(curr,path,start):
            if curr == 0:
                #print("leaf")
                out.append(path[:])
                return
            elif curr < 0:
                return
            for i in range(start,end):
                path.append(nums[i])
                #print(nums[i],path,curr)     
                dfs(curr - nums[i],path,i)
                path.pop()
        
        dfs(target,path,0)
        return out
            
        