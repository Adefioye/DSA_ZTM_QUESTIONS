from collections import deque

testMatrix = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]
];

# def BFS_twoD(matrix):
#     result = []
#     queue = [(0, 0)]
#     visited = set()
#     row_size = len(matrix)
#     col_size = len(matrix[0])
#     dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

#     while len(queue) > 0:
#         r, c = queue.pop(0)

#         for dir in dirs:
#             row = r + dir[0]
#             col = c + dir[1]

#             if row < 0 or row >= row_size or col < 0 or col >= col_size or (row, col) in visited:
#                 continue

#             queue.append((row, col))
#             visited.add((row, col))
#             result.append(matrix[row][col])

#     return result 


# print(BFS_twoD(testMatrix))

def find_bfs(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    visited = set()
    result = []
    queue = deque()
    queue.append((0, 0))
    visited.add((0, 0))
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        curPosition = queue.popleft()
        r, c = curPosition
        result.append(matrix[r][c])
        
        for dir in dirs:
            row = r + dir[0]
            col = c + dir[1]

            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited:
                continue 
            
            queue.append((row, col))
            visited.add((row, col))

    return result


print(find_bfs(testMatrix))