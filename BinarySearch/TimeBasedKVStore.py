from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store[key]
        l = 0 
        r = len(vals) - 1
        val = ""
        while l <= r: 
            mid = (l + r) // 2
            if vals[mid][0] == timestamp:
                return vals[mid][1]
            elif vals[mid][0] < timestamp: 
                val = vals[mid][1]
                l = mid + 1 
            else: 
                r = mid - 1
        
        return val
