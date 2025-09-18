# Definition for a binary tree node.
from typing import Optional


from typing import Optional, List
from collections import deque


class TreeNode:
    """Задание ноды"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Решение максимального глубины дерева"""

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# функция для построения дерева из списка
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Функция для построения дерева из списка"""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:  # левый ребёнок
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:  # правый ребёнок
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# входные данные
arr = [3, 9, 20, None, None, 15, 7]
tree = build_tree(arr)

sol = Solution()
print(sol.maxDepth(tree))  # должно вывести 3
