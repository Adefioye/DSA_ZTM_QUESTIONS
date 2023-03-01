from collections import deque 


matrix1 = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1]
] # 2

matrix2 = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1]
] # 7

def numIslands(matrix):
    NROWS = len(matrix)
    NCOLS = len(matrix[0])
    islandCount = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for r in range(NROWS):
        for c in range(NCOLS):

            if matrix[r][c] == 1:
                islandCount += 1 
                matrix[r][c] = 0 

                queue = deque()
                queue.append((r, c))
                # visited = set()

                while queue:
                    curRow, curCol = queue.popleft()

                # if row < 0 or row >= NROWS or col < 0 or col >= NCOLS or (row, col) in visited:
                #     continue 

                    for dir in dirs:
                        row = curRow + dir[0]
                        col = curCol + dir[1]

                        if row < 0 or row >= NROWS or col < 0 or col >= NCOLS:
                            continue
                        

                        if matrix[row][col] == 1:
                            queue.append((row, col))
                            matrix[row][col] = 0

    return islandCount


print(numIslands(matrix1))
print(numIslands(matrix2))