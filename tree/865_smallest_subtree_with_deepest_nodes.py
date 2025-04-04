"""
[865] Smallest Subtree with all the Deepest Nodes

--- Medium ---

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depth_first_search(node: Optional[TreeNode], level: int) -> (Optional[TreeNode], int):
    if not node:
        return None, level - 1

    if not node.left and not node.right:
        return node, level

    left_lca, left_depth = depth_first_search(node.left, level + 1)
    right_lca, right_depth = depth_first_search(node.right, level + 1)

    if left_depth == right_depth:
        return node, left_depth

    elif left_depth > right_depth:
        return left_lca, left_depth

    else:
        return right_lca, right_depth


def lca_deepest_leaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    lca, depth = depth_first_search(root, 0)
    return lca
