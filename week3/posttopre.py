def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return []

    # The first element in preorder is the root of the tree
    root_val = preorder[0]
    root_index = inorder.index(root_val)

    # Split the inorder array into left and right subtrees
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    # Find the left and right preorder by slicing based on left and right inorder arrays
    left_preorder = []
    right_preorder = []

    # Split the preorder array into left and right subtrees
    for node in preorder[1:]:
        if node in left_inorder:
            left_preorder.append(node)
        else:
            right_preorder.append(node)

    # Recursively build the left and right trees
    left_tree = build_tree(left_preorder, left_inorder)
    right_tree = build_tree(right_preorder, right_inorder)

    # Combine to form the complete level-order array
    result = [root_val]
    result.extend(left_tree)
    result.extend(right_tree)

    return result


def level_order_array(preorder, inorder):
    return build_tree(preorder, inorder)


# Given traversals
preorder = [1, 2, 4, 5, 3]
inorder = [4, 2, 5, 1, 3]

# Get the array representation
result = level_order_array(preorder, inorder)
print(result)
