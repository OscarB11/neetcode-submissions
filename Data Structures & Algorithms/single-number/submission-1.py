from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        item_count  = Counter(nums)
        #print(item_count)

        out = []

        for item, count in item_count.items(): 
            if count == 1:
                return item
                
        