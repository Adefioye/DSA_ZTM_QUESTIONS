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
    row_size = len(matrix)
    col_size = len(matrix[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    result = []
    visited = set()
    queue = [(0, 0)]

    while len(queue) > 0:
        row, col = queue.pop(0)

        print(row, col)

        for dir in dirs:
            r = row + dir[0]
            c = col + dir[1]

            if r < 0 or r >= row_size or c < 0 or c >= col_size or (r, c) in visited:
                continue 

            queue.append((r, c))
            visited.add((r, c))
            result.append(matrix[r][c])

    return result


print(find_bfs(testMatrix))