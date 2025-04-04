"""
[1123] Lowest Common Ancestor of Deepest Leaves

--- Medium ---

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

- The node of a binary tree is a leaf if and only if it has no children

- The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.

- The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
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
