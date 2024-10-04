from typing import Optional
from Tree import TreeNode

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None: 
            return None

        left = None 
        right = None

        if root.left is not None: 
            left = self.invertTree(root.left)

        if root.right is not None:
            right = self.invertTree(root.right)

        root.right = left 
        root.left = right 
        return root