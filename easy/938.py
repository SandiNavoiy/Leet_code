
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:


        def dfs(node, low, high):
            if node is None:
                return 0
            s = 0
            if low <= node.val <= high:
                s += node.val
            s += dfs(node.left, low, high)
            s += dfs(node.right, low, high)
            return s


        return dfs(root, low, high)
