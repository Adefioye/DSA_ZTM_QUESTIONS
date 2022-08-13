testMatrix = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]
];

# def twoD_dfs(matrix):
#     row_size = len(matrix)
#     col_size = len(matrix[0])
#     visited = set()
#     result = []

#     def dfs(row, col, visited):
#       result.append(matrix[row][col])  
#       visited.add((row, col))
#       directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

#       for dir in directions:
#         r = row + dir[0]
#         c = col + dir[1]

#         if r < 0 or r >= row_size or c < 0 or c >= col_size or (r, c) in visited:
#           continue

#         dfs(r, c, visited)

#     dfs(0, 0, visited)
#     return result

# print(twoD_dfs(testMatrix))

def find_dfs(matrix):
  row_size = len(matrix)
  col_size = len(matrix[0])
  visited = set()
  result = []
  dirs = [(-1, 0), (0, 1), (1, 0), [0, -1]]

  def dfs(row, col, visited):
    visited.add((row, col))
    result.append(matrix[row][col])

    for dir in dirs:
      r = row + dir[0]
      c = col + dir[1]

      if r < 0 or r >= row_size or c < 0 or c >= col_size or (r, c) in visited:
        continue
      
      dfs(r, c, visited)

  dfs(0, 0, visited)
  return result


print(find_dfs(testMatrix))
