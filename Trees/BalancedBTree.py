from typing import Optional 
from Tree import TreeNode


def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balanced = True

        def dfs(curr):
            if curr is None: 
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            if abs(left - right) > 1:
                self.balanced = False

            return max(left, right) + 1

        dfs(root)
        return self.balanced