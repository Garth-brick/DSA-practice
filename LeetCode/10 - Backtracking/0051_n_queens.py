from typing import List, Set, Tuple


""" NOTE
- If a square is unattacked, place a queen there and mark all the squares that it is attacking
- Go to the next unattacked square and place a queen there as well
- If you manage to place all queens before reaching the end of the board then you have a valid answer
- If you reach the end of the board without having placed all queens then remove the last queen you placed and move it to the next unattacked square

OPTIMISATION:
- If you want to place n queens in n rows then the each row must have exactly one queen
- This means that we just need to figure out the positions for each queen within its own row
- So if any one row becomes completely attacked then thats a fail-case
"""


def solveNQueens(n: int) -> List[List[str]]:
    
    # a list of lists of strings to store the result
    result: List[List[str]] = []
    
    # array to store how many queens are attacking a particular position
    attacked = [[0 for _ in range(n)] for _ in range(n)]
    
    # method to change that array which holds how many attacks are being made at a given square
    # if we want to remove a queen then we set placing=False
    def alterAttacks(row, col, placing=True):
        placeOrRemove = 1 if placing else -1
        for r in range(n):
            for c in range(n):
                if r == row or c == col or r + c == row + col or r - c == row - col:
                    attacked[r][c] += placeOrRemove
    
    
    def newAnswer(queenPositions):
        answerList = []
        for r in range(n):
            answerRow = ''
            for c in range(n):
                if (r, c) in queenPositions:
                    answerRow += 'Q'
                else:
                    answerRow += '.'
            answerList.append(answerRow)
        result.append(answerList)
        
    
    def placeQueen(row: int, col:int, queenPoistions: Set[Tuple[int, int]]):
        

        
        if row >= n or col >= n or row < 0 or col < 0:
            return
        
        # if this position is attacked then look at the next position in the same row
        if attacked[row][col]:
            # since there must be a queen in each row
            # try placing a queen in the same row in the next column
            return
        else:
            # if it is a free square then place a queen there
            queenPoistions.add((row, col))
            
            # mark all the other square which are now attacked by this queen
            alterAttacks(row, col, placing=True)
            
            # if we now have n queens then add this to the result
            if len(queenPoistions) == n:
                newAnswer(queenPoistions)
            else:
                # try placing a queen in the next row now
                for c in range(n):
                    placeQueen(row+1, c, queenPoistions)
                
            # removing the queen we just placed to try out the next position
            queenPoistions.remove((row, col))
            alterAttacks(row, col, placing=False)
        
    
    for col in range(n):
        placeQueen(0, col, set())
    
    return result

print(solveNQueens(4))