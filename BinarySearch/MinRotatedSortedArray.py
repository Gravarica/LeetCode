from typing import List

def findMin(nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1 
        
        if len(nums) == 1:
            return nums[0]

        while l < r: 
            mid = (l + r) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid - 1
        
        return nums[l]
            
            
arr1 = [7, 8, 9, 1, 2, 3, 4, 5, 6]
arr2 = [1, 2, 3, 4, 5, 6]
arr3 = [2, 1]
arr4 = [3, 4, 5, 6, 1, 2]
arr5 = [7, 1, 2, 3, 4, 5, 6]
# print(findMin(arr5))

arr6 = [295,298,299,4,10,13,15]
print(arr6[(len(arr6) - 1) // 2])