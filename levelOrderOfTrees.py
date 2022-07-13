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

#------------------------------------------------------------------------------
# ZTM FIRST SOLUTION
#-------------------------------------------------------------------------------


def level_order_trees(root):

    res = []
    queue = [root]

    while len(queue) > 0:
        count = 0
        length = len(queue)
        current_level_arrays = []

        while count < length:
            current_node = q.pop(0)
            current_level_arrays.append(current_node.value)
            count += 1

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        res.append(current_level_arrays)

    return res