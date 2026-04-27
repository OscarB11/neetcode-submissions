class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dset = set(nums)

        if len(nums) > len(dset):
            #print len(nums),len(dset)
            return  True
        else:
            return False