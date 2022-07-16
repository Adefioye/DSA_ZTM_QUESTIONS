#-------------------------------------------------------------------------------------
# MY 1ST SOLUTION
#-------------------------------------------------------------------------------

def get_num_of_nodes(root):

    if root == None:
        return 0

    height = get_height_of_tree(root)

    upper_count = 2 ** height - 1 

    while left < right:
        idx_to_find = ((left + right) // 2) + 1 

        if node_exists(idx_to_find, height, root):
            left = idx_to_find 
        else:
            right = idx_to_find - 1

    return upper_count + left + 1 

def get_height_of_tree(root):
    height = 0

    while root:
        height += 1 
        root = root.left

    return height

def node_exists(idx_to_find, height, node):

    left = 0 
    right = 2 ** height - 1 

    while left < right:
        mid = ((left + right) // 2) + 1 

        if idx_to_find >= mid:
            node = node.right 
            left = mid 
        else:
            node = node.left 
            right = mid - 1

    return node != None