class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()
        for nums in board:
            #print(nums)
            for i in nums:
                #print(i)
                if i in seen:
                    return False  
                if i != ".":
                    seen.add(i)
            seen.clear()

        #print("\n\n")

        for i in range(len(board)):
            for col in board:
                #print(col[i])
                #print(seen2)
                if col[i] in seen:
                    #print("dupe found")
                    return False  
                if col[i] != ".":
                    seen.add(col[i])
            seen.clear()
            
            #print("\n")
        

        for box_row in range(0, 9, 3):  # Loop through each 3x3 sub-box row
            for box_col in range(0, 9, 3):  # Loop through each 3x3 sub-box column
                for i in range(3):  # Loop within the 3x3 sub-box
                    for j in range(3):
                        num = board[box_row + i][box_col + j]
                        if num in seen:
                            return False  # Duplicate found in the sub-box
                        if num != ".":
                            seen.add(num)
                seen.clear()  # Clear the set for the next 3x3 sub-box

    
        
        return True
        