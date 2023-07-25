from typing import List


def numIslands(grid: List[List[str]]) -> int:
    result: int = 0
    ROWS = len(grid)
    COLS = len(grid[0])
    DELTAS = ((1,0), (0,1), (-1,0), (0,-1)) # Tuple(rowDelta, columnDelta)
    # visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    
    def bfs(row, col):
        if (row < 0 or col < 0 or
            row >= ROWS or col >= COLS or
            grid[row][col] == "0"):
            # if we have come off the island
            return
        
        # if we are still on the island
        # make this cell visited by turning it into a zero
        grid[row][col] = "0"
        
        # check the 4 adjacent cells if they are part of the same island and should be marked as visited
        for DELTA in DELTAS:
            bfs(row + DELTA[0], col + DELTA[1])
            
    
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "1":
                result += 1
                bfs(row, col)
        
    return result

grid = [["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]]
print(numIslands(grid))