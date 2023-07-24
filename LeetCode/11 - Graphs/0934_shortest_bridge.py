import collections
from typing import List, Tuple, Set, Dict, Optional

def shortestBridge(grid: List[List[int]]) :
    
    LAND = 1
    WATER = 0
    ROWS = len(grid)
    COLS = len(grid[0])
    DELTAS = ((0,1), (1,0), (0,-1), (-1,0))
    visited = set()
    
    def getCoordsOfOneIsland(row, col) -> Set[Tuple[int, int]]:
        tempQ: collections.deque[Tuple[int, int]] = collections.deque()
        tempQ.append((row, col))
        visited.add((row, col))
        
        while tempQ:
            row, col = tempQ.popleft()
            
            for DELTA_ROW, DELTA_COL in DELTAS:
                newRow = row + DELTA_ROW
                newCol = col + DELTA_COL
                if (newRow in range(ROWS) and newCol in range(COLS) and
                    grid[newRow][newCol] and (newRow, newCol) not in visited):
                    tempQ.append((newRow, newCol))
                    visited.add((newRow, newCol))
        return visited
    
    q = None    
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] and (row, col) not in visited:
                q = collections.deque(getCoordsOfOneIsland(row, col))
                break
        if q: 
            break
    
    # now searching for the distance to the next island
    
    distance = 0
    while q:
        for _ in range(len(q)):
            row, col = q.popleft()
            
            for DELTA_ROW, DELTA_COL in DELTAS:
                newRow = row + DELTA_ROW
                newCol = col + DELTA_COL
                if (newRow in range(ROWS) and newCol in range(COLS) and 
                    (newRow, newCol) not in visited):
                    if grid[newRow][newCol] == LAND:
                        return distance
                    q.append((newRow, newCol))
                    visited.add((newRow, newCol))
        distance += 1
    return -1

grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,0,0,0]
    ]
print(shortestBridge(grid))