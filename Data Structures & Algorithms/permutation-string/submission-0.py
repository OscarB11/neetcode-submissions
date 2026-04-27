
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        windowCount = Counter(s2[:len(s1)])
        
        if s1Count == windowCount:
            return True

        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]
            end_char = s2[i]

            windowCount[end_char] += 1
            windowCount[start_char] -= 1

            if windowCount[start_char] == 0:
                del windowCount[start_char]
            
            if windowCount == s1Count:
                return True
        
        return False
