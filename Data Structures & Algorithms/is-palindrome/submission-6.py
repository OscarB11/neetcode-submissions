class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        news = ""

        for i in s:
            if i.isalnum():
                news+= i.lower()

        l = 0
        r = len(news)-1

        while l<r:

            if news[l] == news[r]:
                l+=1
                r-=1
            else:
                #print(news[l] , news[r])
                return False
        
        return True


        