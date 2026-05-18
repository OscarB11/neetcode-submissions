class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        self.out = []

        def dfs(curr,ind):
            if len(curr) == len(digits):
                ans = "".join(curr)
                self.out.append(ans)
                return

            base = letters[digits[ind]]
            for i in base:
                #print(base,i)
                curr.append(i)
                dfs(curr,ind+1)
                curr.pop()
        

        dfs([],0)
        return  self.out
