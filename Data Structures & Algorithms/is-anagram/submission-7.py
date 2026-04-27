class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        scount = {}
        tcount = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            scount[s[i]] = scount.get(s[i],0)+ 1
            tcount[t[i]] = tcount.get(t[i],0)+ 1
        
        return scount == tcount 

        