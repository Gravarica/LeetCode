
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order

# Example 1

# # # input: nums = [1,2,2,3,3,3], 
# # # k = 2
# # # Output: [2,3]

# Example 2

# # # input: nums = [7,7],
# # # k = 1
# # # Output: [7]

##### DIFF: MEDIUM

from typing import List


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyTable = {}
        kvalues = [[] for i in range(len(nums) + 1)]

        for element in nums: 
            if element in frequencyTable: 
                frequencyTable[element] += 1
            else: 
                frequencyTable[element] = 1
        
        for key, value in frequencyTable.items(): 
            kvalues[value].append(key)
        
        #[1, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 8, 9, 9, 9, 9]
        # k = 3
        # freqTable = { 1: 1, 3: 3, 4: 3, 5: 4, 6: 4, 7: 1, 8: 1, 9: 4} 
        # kvalues = { 0: [], 1: [1, 7, 8]: 2: [], 3: [3, 4], 4: [5, 6, 9], ...}

        res = [] 
        for i in range(len(kvalues) - 1, 0, -1):
            for n in kvalues[i]:
                res.append(n)
                if len(res) == k:
                    return res