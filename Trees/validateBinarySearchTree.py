def isBST(root, min, max):

    if root == None:
        return True 

    if (root.value > min) and (root.value < max) and isBST(root.left, min, root.value) and isBST(root.right, root.data, max):
        return True

    return False

print(isBST(root, float("-inf"), float("inf")))