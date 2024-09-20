from typing import List

def trap(height: List[int]) -> int: 

    maxLefts = [0] * len(height)
    maxLefts[0] = height[0]
    for i in range(1, len(height)): 
        maxLefts[i] = max(maxLefts[i - 1], height[i])
    
    maxRights = [0] * len(height)
    maxRights[-1] = height[-1]
    for i in range(len(height) - 2, -1, -1):
        maxRights[i] = max(maxRights[i + 1], height[i])

    result = 0 
    for i in range(len(height)):
        result += max(min(maxLefts[i], maxRights[i]) - height[i], 0)

    return result

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))