class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana ={}
        for i in strs:
            uid = "".join(sorted(i))
            if uid not in ana:
                ana[uid] = []
            
            ana[uid].append(i)

        output = []
        print(ana)
        for x in ana:
            
            v = ana[x]
            
            output.append(v)


        return output 