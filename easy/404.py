# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        rez = 0
        if root.left:
            if not root.left.left and not root.left.right:
                rez += root.left.val
            else:
                rez += self.sumOfLeftLeaves(root.left)

        rez += self.sumOfLeftLeaves(root.right)

        return rez
