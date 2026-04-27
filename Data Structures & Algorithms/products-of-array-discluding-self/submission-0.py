class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        out = []
        pre = []
        suff = []
        index = len(nums)
        prefix = 1
        suffix =1

        for i in range(index):
            print(nums[i])

            if i == 0 :
                prefix = 1
            else:
                prefix *= nums[i-1]
            
            print("pre",prefix)
            pre.append(prefix)

        print("suffix")
        for i in range(index-1,-1,-1):
            print(i,nums[i])

            if i == index-1 :
                suffix = 1
            else:
                suffix *= nums[i+1]
               
            
            print("suff",suffix)
            suff.insert(0,suffix)

        print("\n",pre,"\n",suff)

        for i in range(index):
            result = pre[i] * suff[i]
            out.append(result)

        print(out)
        return out

        