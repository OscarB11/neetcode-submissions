class Solution:
    def reverseBits(self, n: int) -> int:
         bi = bin(n)[2:]
         zeros = 32 - len(bi)
         old = zeros*"0"+bi
         new =  old[::-1]
         print(bi,old,new)
         out  = 0
         val = 1

         for i in range(len(new)-1,-1,-1):
            print(new[i])
            if new[i] == "1":
                out +=val
            val = val*2

         return out
        