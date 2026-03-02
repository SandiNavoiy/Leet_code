class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def build_tree(lst):
    root = None
    for v in lst:
        root = insert(root, v)
    return root


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print("   " * level + str(node.value))
        print_tree(node.left, level + 1)


data = [1, -4, 5, 6, 0, 7, 124, 7]

root = build_tree(data)
print_tree(root)