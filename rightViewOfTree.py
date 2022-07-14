#-------------------------------------------------------------------------------------
# MY 1ST SOLUTION
#-------------------------------------------------------------------------------
# BFS APPROACH
def bfs_tree_right_view(root):
    
    if root == None:
        return []
    
    queue = [root]
    nums_on_right_view = [] # Pop last item on each level to the right

    while len(q) > 0:
        nums_on_current_level = []
        count = 0
        queue_length = len(q) 

        while count < queue_length:
            current_node = queue.pop(0) 
            count += 1
            nums_on_current_level.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        # Add last item of the numbers on each level to the array for right view nodes
        nums_on_right_view.append(nums_on_current_level.pop())

    return nums_on_right_view

# DFS APPROACH

def dfs_right_side_view(root, level=0):

    res = []
    dfs(root, level, res)
    return res

def dfs(root, level, res):

    if root == None:
        return 

    if level == len(res):
        res.append(root.value)

    if root.right:
        dfs(root.right, level + 1, res)

    if root.left:
        dfs(root.left, level + 1, res)





