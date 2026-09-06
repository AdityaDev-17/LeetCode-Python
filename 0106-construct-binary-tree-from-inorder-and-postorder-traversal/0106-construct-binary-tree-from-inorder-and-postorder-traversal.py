# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Store inorder value -> index
        inorder_index = {}

        for i in range(len(inorder)):
            inorder_index[inorder[i]] = i

        postorder_index = len(postorder) - 1

        def build(left, right):
            nonlocal postorder_index

            if left > right:
                return None

            # Last element in postorder is the root
            root_value = postorder[postorder_index]
            postorder_index -= 1

            root = TreeNode(root_value)

            # Find root in inorder
            mid = inorder_index[root_value]

            # Build right subtree first
            root.right = build(mid + 1, right)

            # Then build left subtree
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)