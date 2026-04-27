class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n= len(heights)
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                width = i -index
                area = height* width 
                maxArea = max(maxArea,area)

                start = index
            stack.append((start, h))

        for i, h in stack:
            area = h * (n-i)
            maxArea = max(maxArea, area)
        
        return maxArea
        