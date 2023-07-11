from typing import List, Set, Tuple


def exist (board: List[List[str]], word: str) -> bool:
    usedCoordinates: Set[Tuple[int, int]] = set()
    ROWS = len(board)
    COLS = len(board[0])
    deltas = ((-1,0), (0,-1), (1,0), (0,1))
    
    def dfs(row: int, col: int, i: int):
        # row and col will provide the coordinates
        # 'i' indicates the index of the character which we are currently checking for
        
        if i >= len(word):
            # if i is greater than the length of the word then we must've already traversed all of the letters in the word
            return True
        
        if (row < 0 or col < 0 or
            row >= ROWS or col >= COLS or
            (row, col) in usedCoordinates or
            board[row][col] != word[i]):
            # if the dfs in this direction is invalid
            return False
        
        # if the dfs in this direction is valid
        # we need to add the current coordinated to the set
        usedCoordinates.add((row, col))
        
        # checking in all four directions
        result = False
        for delta in deltas:
            result = result or dfs(row + delta[0], col + delta[1], i + 1)
            if result: break
        
        # if none of the paths worked out then we need to remove the current coordinate before calling dfs again
        if not result:
            usedCoordinates.remove((row, col))
        
        return result

    for row in range(ROWS):
        for col in range(COLS):
            if dfs(row, col, 0):
                return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word)) # true