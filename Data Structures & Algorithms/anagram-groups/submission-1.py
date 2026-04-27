from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        out = []
        work = strs

        for i in strs:
            ic = Counter(i)
            #print(i,ic)

            T = False
            position = 0

            for s in range(len(out)):
                sa = out[s][0]
                sc = Counter(sa)
                #print(s,sa,sc,ic)
                if sc == ic:
                    T = True
                    print("true",T)
                    positon = s
                    break
            
            if T != True:
                entry = []
                entry.append(i)
                out.append(entry)
                #print("test",out)
            else:
                out[positon].append(i)


            


        return out
        