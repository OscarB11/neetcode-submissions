class Solution:

    def encode(self, strs: List[str]) -> str:
        print("hello")
        res = ""
        
        for i in strs:
            res += i 
            res += " @£"

        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        out = []
        count = 0 

        for i in range(len(s)):
            if s[i] == "£" and s[i-1] == "@":
                out.append(s[count:i-2])
                count = i+1

        print(out)

        return out
