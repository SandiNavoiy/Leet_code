class Node:
    """
    Класс узла дерева.
    """

    def __init__(self, key, value):
        # Ключ.
        self.key = key
        # Значение.
        self.value = value
        # Потомки.
        self.children = []


def find(node, x):
    if node.key == x:
        return node.value
    else:
        for child in node.children:
            result = find(child, x)
            if result is not None:
                return result

            # Если узел с таким ключом не найден.
    return None


# Создаём дерево
root = Node("a", "A")
node_b = Node("b", "B")
node_c = Node("c", "C")
node_d = Node("d", "D")
node_i = Node("i", "I")

root.children.extend([node_b, node_c, node_d])
node_b.children.extend([Node("e", "E")])
node_c.children.extend([Node("f", "F"), Node("g", "K")])
node_d.children.extend([Node("h", "H"), node_i, Node("k", "K")])
node_i.children.extend([Node("l", "L"), Node("m", "M"), Node("n", "N"), Node("o", "O")])

# Ищем элемент с ключом m
result = find(root, "m")
print(result)
