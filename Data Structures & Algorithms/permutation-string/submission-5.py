
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        windowCount = Counter(s2[:len(s1)])

        if s1Count == windowCount:
            return True

        for i in range(len(s1), len(s2)):
        

            l = s2[i - len(s1)]
            r = s2[i]

            windowCount[r] += 1
            windowCount[l] -= 1

            if windowCount[l] == 0:
                del windowCount[l]
            
            if windowCount == s1Count:
                return True
        
        return False
