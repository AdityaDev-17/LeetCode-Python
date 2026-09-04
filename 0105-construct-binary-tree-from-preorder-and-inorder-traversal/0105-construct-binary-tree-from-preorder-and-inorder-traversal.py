# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {}

        for i in range(len(inorder)):
            inorder_index[inorder[i]] = i

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            # First element in preorder is the root
            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            # Find root position in inorder
            mid = inorder_index[root_value]

            # Build left subtree first
            root.left = build(left, mid - 1)

            # Then build right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)