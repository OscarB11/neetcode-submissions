class Solution:
    def hammingWeight(self, n: int) -> int:
        bi =  bin(n)[2:]
        count = 0 
        for i in bi:
            if i == "1":
                count+=1
        return count
        