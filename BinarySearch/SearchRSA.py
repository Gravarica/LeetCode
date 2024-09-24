from typing import List 

def findMin(nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1 
    
    if len(nums) == 1:
        return 0

    while l < r: 
        mid = (l + r) // 2
        if nums[mid] < nums[mid - 1]:
            return mid
        if nums[mid] > nums[r]:
            l = mid + 1
        elif nums[mid] < nums[r]:
            r = mid - 1
    
    return l

def search(nums: List[int], target: int) -> int:
    r = len(nums) - 1 
    minInd = findMin(nums)
    l = minInd
    result = -1
    while l <= r: 
        mid = (l + r) // 2 
        
        if nums[mid] == target: 
            result = mid
            break
        elif nums[mid] < target: 
            l = mid + 1
        else: 
            r = mid - 1

    if result == -1: 
        l = 0
        r = minInd
        while l <= r: 
            mid = (l + r) // 2 
            
            if nums[mid] == target: 
                result = mid
                break
            elif nums[mid] < target: 
                l = mid + 1
            else: 
                r = mid - 1

    return result

arr1 = [4, 5, 6, 7, 0, 1, 2]
arr2 = [1]
print(search(arr2, 1))