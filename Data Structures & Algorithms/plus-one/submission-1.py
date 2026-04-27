class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)     

        print(s)
        out = int(s)+1
        print(out)
        sout = str(out)

        res= []

        for i in sout:
            res.append(i)

        return res