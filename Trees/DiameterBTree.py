from typing import Optional 
from Tree import TreeNode

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if curr is None:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            self.res = max(self.res, left + right)

            return max(left, right) + 1

        dfs(root)
        return self.res