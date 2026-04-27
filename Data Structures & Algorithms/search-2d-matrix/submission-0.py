class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        nums = [num for row in matrix for num in row]
        print(nums)  # Output: [1, 2, 4, 8, 10, 11, 12, 13, 14, 20, 30, 40]

        
        l = 0
        r = len(nums)-1

        while l <= r:
            
            mid = l + ((r - l) // 2)  
            

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return True
        
        return False
        