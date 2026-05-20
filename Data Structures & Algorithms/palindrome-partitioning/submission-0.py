class Solution:
    def partition(self, s: str) -> List[List[str]]:

        out = []
        curr = []

        def ispalidrome(s,l,r):
            while l < r:
                if s[l] != s[r]:
                    return False 
                l+=1
                r-=1
            return True


        def dfs(i):
            if i >= len(s):
                out.append(curr[:])
                return

            for c in range(i,len(s)):
                if ispalidrome(s,i,c):
                    curr.append(s[i:c+1])
                    dfs(c+1)
                    curr.pop()


            
        

        dfs(0)
        return out
        