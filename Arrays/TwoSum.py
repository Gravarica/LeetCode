from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {} 

    for i, n in enumerate(nums):
        complement = target - n 
        if complement in prevMap: 
            return [prevMap[complement], i]
        else: 
            prevMap[n] = i