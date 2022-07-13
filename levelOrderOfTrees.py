#------------------------------------------------------------------------------
# MY FIRST SOLUTION
#-------------------------------------------------------------------------------


def level_order_trees(root):

    res = []
    q = [root]

    while len(q) > 0:

        num_count_by_level = len(q)
        array_by_level = []
        nodes_on_next_level = []

        for i in range(num_count_by_level):
            current_node = q.pop(0)
            array_by_level.append(current_node.value)

            if current_node.left:
                nodes_on_next_level.append(current_node.left)
            
            if current_node.right:
                nodes_on_next_level.append(current_node.right)

        q = nodes_on_next_level

        res.append(array_by_level)

    return res