from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        print(freq)

        freq_values = sorted(freq.values())
        print(freq_values[-k:])

        top_k_values = freq_values[-k:]
        
        top_k_keys = []
        for key, value in freq.items():
            if value in top_k_values:
                top_k_keys.append(key)



        return top_k_keys
        