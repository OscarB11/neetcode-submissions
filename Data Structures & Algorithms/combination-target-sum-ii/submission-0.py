class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        out = []
        
        def dfs(start, path, remaining):
            if remaining == 0: 
                out.append(path[:])
                return
            
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                c = candidates[i]
                if remaining < candidates[i]:
                    break
    
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                else:
                    path.append(c)
                    dfs(i+1, path, remaining - c)  
                    path.pop()

        dfs(0, [], target)
        return out