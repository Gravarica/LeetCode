from typing import List

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [element for row in matrix for element in row]

        l = 0 
        r = len(arr) - 1

        while l <= r:
            half = (l + r) // 2 
            if arr[half] == target: 
                return True
            elif arr[half] > target:
                r = half - 1
            else: 
                l = half + 1

        return False 