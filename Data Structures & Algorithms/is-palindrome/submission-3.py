class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0 
       
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        right = len(s)-1

        if not s:
            return True

        print(right)
        print(s,s[right])

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
        