from typing import List 

def threeSum(nums: List[int]) -> List[List[int]]:

    result = [] 
    nums = sorted(nums)

    for i, val in enumerate(nums): 

        if val > 0: 
            break 

        if i > 0 and nums[i] == nums[i - 1]:
            continue 
    
        l = i + 1 
        r = len(nums) - 1
        target = -val

        while l < r: 

            comp = nums[l] + nums[r]
            if comp > target: 
                r -= 1
            elif comp < target: 
                l += 1
            else: 
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    return result 