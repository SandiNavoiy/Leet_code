# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        ''''''
        return root.val==root.left.val+root.right.val

# Создаем дерево
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)

# Проверяем дерево
s = Solution()
print(s.checkTree(root))  # True, потому что значения в левом