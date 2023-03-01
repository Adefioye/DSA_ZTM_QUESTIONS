from collections import deque

matrix1 = [
    [2, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1]
] # 7

matrix2 = [
    [1, 1, 0, 0, 0],
    [2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2],
    [0, 1, 0, 0, 1]
] # -1

matrix3 = [
    [2, 0, 1, 0, 0],
    [1, 1, 0, 0, 2],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1]
] # -1

def rottenOranges(matrix):

    NROWS = len(matrix)
    NCOLS = len(matrix[0])
    numFreshOranges = 0
    queue = deque() # For getting initial positions of rotten oranges(2) in the matrix
    numOfMinutes = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    for r in range(NROWS):
        for c in range(NCOLS):

            if matrix[r][c] == 1:
                numFreshOranges += 1 

            if matrix[r][c] == 2:
                queue.append((r, c))

    # We have nums of fresh oranges and starting positions of rotten oranges
    # We are gonna perform bfs to compute minutes needed to rotten all oranges
    # AS we rotten fresh oranges level by level we decrement adjacent fresh oranges
    # and increment num of minutes after processing rotten oranges at each level of BFS traversal
    # print(f"Original fresh oranges: {numFreshOranges}")
    while queue:

        for _ in range(len(queue)):
            currentPos = queue.popleft()

            for dir in directions:
                row = currentPos[0] + dir[0]
                col = currentPos[1] + dir[1]

                # Check if there are fresh oranges adjacent 
                # and rotten them and add position to queue
                # As fresh orange rotten, we decrement num of fresh oranges
                # After processing all positions in queue at this level, we increment num of minutes
                if row < 0 or row >= NROWS or col < 0 or col >= NCOLS:
                    continue 

                if matrix[row][col] == 1:
                    matrix[row][col] = 2
                    numFreshOranges -= 1
                    queue.append((row, col))

        numOfMinutes += 1

    # print(f"Num of mins: {numOfMinutes}, Remaining Fresh oranges: {numFreshOranges}")
    if numFreshOranges > 0:
        return -1

    return numOfMinutes - 1 

print(rottenOranges(matrix1))
print(rottenOranges(matrix2))
print(rottenOranges(matrix3))

