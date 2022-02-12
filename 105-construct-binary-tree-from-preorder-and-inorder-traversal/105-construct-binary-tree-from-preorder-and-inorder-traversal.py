class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder,inorder[:index])
            node.right = self.buildTree(preorder,inorder[index+1:])
            
            return node