class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0 
        r= 0 
        maxl = 0
        cset = set()
        

        while r < len(s):
            if s[r] not in cset:
                cset.add(s[r])
                maxl = max(maxl,r-l+1)
                r+=1
            else:
                cset.remove(s[l])
                l+=1
        return maxl
        