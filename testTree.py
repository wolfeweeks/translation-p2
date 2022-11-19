def printPreorder(root, depth):
    if root:
        # root.write(file)
        root.write(depth)
        if root.children is not None:
            for child in root.children:
                printPreorder(child, depth + 1)