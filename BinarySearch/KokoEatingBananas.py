from typing import List
from math import ceil

def minEatingSpeed(piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r: 
            k = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += ceil(float(p) / k)
            if totalTime <= h: 
                res = k 
                r = k - 1
            else: 
                l = k + 1
        
        return res
        
        

arr = [4, 11, 20, 23, 30]

h = 6
avgSpeed = ceil(sum(arr)) / h
print(minEatingSpeed(arr, h))