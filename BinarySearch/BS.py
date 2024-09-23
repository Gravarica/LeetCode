from typing import List

def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        half = (l + r) // 2

        if nums[half] == target:
            return half
        elif nums[half] > target: 
            r = half - 1
        else: 
            l = half + 1

    return -1    

nums = [-1,0,3,5,9,12]
val = search(nums, -1)
print(val) 