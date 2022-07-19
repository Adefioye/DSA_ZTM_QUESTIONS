#-------------------------------------------------------------------------------------
# 1ST SOLUTION
#-------------------------------------------------------------------------------
def height_of_tree(node, count):

    if node == None:
        return count 

    count += 1 

    return max(height_of_tree(node.left, count), height_of_tree(node.right, count))