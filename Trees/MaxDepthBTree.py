from typing import Optional 
from Tree import TreeNode

def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None: 
            return 0 

        maxVal = max(self.maxDepth(root.left), self.maxDepth(root.right))

        return 1 + maxVal