from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    result: List[List[str]] = []
    
    # two queens should not be in the same row or column and the values of their (row+col) and (row-col) must also be different
    usedCols = set()
    usedSums = set() # row + col
    usedDiffs = set() # row - col
    
    # creating a board in the required format with '.'
    # using a list because we want to be able to edit it later
    board = [['.'] * n for _ in range(n)]
    
    # backtracking function to check row by row
    def backtrack(row):
        if row >= n:
            boardCopy = ["".join(r) for r in board]
            result.append(boardCopy)
            return
        
        # trying each position in the current row
        for col in range(n):
            
            if (col in usedCols or (row + col) in usedSums or 
                (row - col) in usedDiffs):
                # if this position is already under attack
                continue
            
            # if this position is not already under attack
            # then place a queen here and add it to all the sets
            usedCols.add(col)
            usedSums.add(row + col)
            usedDiffs.add(row - col)
            board[row][col] = 'Q'
            
            # check the next row
            backtrack(row + 1)
            
            # if this function returns then we need to reset the queen we just placed
            usedCols.remove(col)
            usedSums.remove(row + col)
            usedDiffs.remove(row - col)
            board[row][col] = '.'
                
    backtrack(0)
    
    return result

print(solveNQueens(4))