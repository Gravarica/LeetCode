from typing import List
from collections import defaultdict

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hashmap = defaultdict(list)

    for s in strs: 
        count = [0] * 26
        for c in s: 
            count[c] += 1
        hashmap[count].append(s)

    return hashmap.values()