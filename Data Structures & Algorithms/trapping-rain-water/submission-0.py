class Solution:
    def trap(self, height: List[int]) -> int:
                L = 0
                R = len(height)-1 

                lmax = height[L]
                rmax = height[R]

                out = 0

                while L < R:
                    if lmax < rmax:
                        L+=1
                        lmax = max(lmax,height[L])
                        out += lmax- height[L]
                    else:
                        R-=1
                        rmax = max(rmax,height[R])
                        out += rmax- height[R]
                return out