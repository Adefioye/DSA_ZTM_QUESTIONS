from collections import deque

INF = float("inf")
GATE = 0
WALL = -1

matrix1 = [
    [INF, WALL, GATE, INF],
    [INF, INF, INF, WALL],
    [INF, WALL, INF, WALL],
    [GATE, WALL, INF, INF]
]
'''
[
    [3, -1, 0, 1],
    [2, 2, 1, -1],
     [1, -1, 2, -1],
     [0, -1, 3, 4]
]
''' 
matrix2 = [
    [INF, WALL, GATE, INF],
    [WALL, INF, INF, WALL],
    [INF, WALL, INF, WALL],
    [GATE, WALL, INF, INF]
]

'''
[
    [inf, -1, 0, 1],
    [-1, 2, 1, -1],
     [1, -1, 2, -1],
     [0, -1, 3, 4]
]
''' 

# BFS SOLUTION for Walls and Gates
def wallsAndGates(matrix):
    NROWS = len(matrix)
    NCOLS = len(matrix[0])
    queue = deque()
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()

    for r in range(NROWS):
        for c in range(NCOLS):

            if matrix[r][c] == GATE:
                queue.append((r, c))
                visited.add((r, c))

    dist = 0
    while queue:
        
        # print(queue, len(queue), dist)
        for _ in range(len(queue)):
            currentPos = queue.popleft()
            curRow, curCol = currentPos 

            matrix[curRow][curCol] = dist 

            for dir in dirs:
                row = curRow + dir[0]
                col = curCol + dir[1]

                if row < 0 or row >= NROWS or col < 0 or col >= NCOLS or (row, col) in visited or matrix[row][col] == WALL:
                    continue 
                
                queue.append((row, col))
                visited.add((row, col))

        dist += 1 

    return matrix 

print(wallsAndGates(matrix1))
print(wallsAndGates(matrix2))

# DFS SOLUTION for Walls and Gates

# def wallAndGates(matrix):
#     NROWS = len(matrix)
#     NCOLS = len(matrix[0])
#     dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#     def dfs(matrix, row, col, numOFSteps):

#         if row < 0 or row >= NROWS or col < 0 or col >= NCOLS or numOFSteps > matrix[row][col]:
#             return 
        
#         matrix[row][col] = numOFSteps 

#         for dir in dirs:
#             dfs(matrix, row + dir[0], col + dir[1], numOFSteps + 1)



#     for r in range(NROWS):
#         for c in range(NCOLS):

#             if matrix[r][c] == GATE:
#                 dfs(matrix, r, c, 0)

#     return matrix 

# print(wallAndGates(matrix1))
# print(wallAndGates(matrix2))

# def wallsAndGates(matrix):

#     NROWS = len(matrix)
#     NCOLS = len(matrix[0])
#     dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


#     def dfs(matrix, row, col, minCount, count, visited, originalPos):

#         if row < 0 or row >= NROWS or col < 0 or col >= NCOLS or (row, col) in visited or matrix[row][col] == WALL:
#             return 
        
#         # either INF or GATE
#         visited.add((row, col))
        
#         if matrix[row][col] == GATE:
#             print(originalPos, count, minCount)
#             if count < minCount:
#                 minCount = count 
#                 originalRowPos = originalPos[0]
#                 originalColPos = originalPos[1]

#                 matrix[originalRowPos][originalColPos] = minCount 
 
#         for dir in dirs:
#             dfs(matrix, row + dir[0], col + dir[1], minCount, count + 1, visited, originalPos)
        

#     for r in range(NROWS):
#         for c in range(NCOLS):

#             if matrix[r][c] == INF:
#                 dfs(matrix, r, c, INF, 0, set(), [r, c])
    
#     return matrix

# print(wallsAndGates(matrix1))
# print(wallsAndGates(matrix2))