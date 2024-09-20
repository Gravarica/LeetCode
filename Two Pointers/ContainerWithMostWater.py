from typing import List

def getArea(tup1, tup2):
    return min(tup1[1], tup2[1]) * (tup2[0] - tup1[0])

def maxArea(heights: List[int]) -> int: 
    
    l = 0
    r = len(heights) - 1
    maxArea = 0

    while l < r: 
        area = getArea((l, heights[l]),(r, heights[r]))
        if area > maxArea: 
            maxArea = area
        
        if heights[l] < heights[r]:
            l += 1
        else: 
            r -= 1

    return maxArea

h =[1,7,2,5,4,7,3,6]
#h = [1, 7, 2, 5, 12, 3, 500, 500, 7, 8, 4, 4, 7, 3, 6]
area = maxArea(h)
print(area)