def tree_intersection(tree1, tree2):
    '''check if the trees have roots'''
    if not tree1.root or not tree2.root:
        return None

    '''recursive helper function to loop through the tree'''
    def recurse(current, action):
        if current.left:
            recurse(current.left, action)
        if current.right:
            recurse(current.right, action)
        action(current)

    '''a set to contain all the unqiue values in tree1'''
    tree_one_set = set()

    '''a helper function that adds values of nodes of a tree to a set'''
    def tree1_action(node):
        nonlocal tree_one_set
        tree_one_set.add(node.value)

    '''fill in tree_one_set with unique values of nodes from tree 1'''
    recurse(tree1.root, tree1_action)

    '''a set to contain all the common values found in tree1 and tree2'''
    common_set = set()

    '''a helper function that compares & adds the common values found in tree_one_set and the node values in tree2. '''
    def tree2_action(node):
        nonlocal tree_one_set, common_set
        if node.value in tree_one_set:
            common_set.add(node.value)

    '''fill in common_set with common values found in tree_one_set and node values in tree2'''
    recurse(tree2.root, tree2_action)

    return common_set
