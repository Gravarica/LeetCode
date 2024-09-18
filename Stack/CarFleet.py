from typing import List

def carFleet(target: int, position: List[int], speed: List[int]):
    pairs = list(zip(position, speed))
    stack = [] 
    for pos, vel in sorted(pairs)[::-1]: 
        time = (target - pos) / vel
        stack.append(time)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop() 
    
    return len(stack)

target=10
position=[8,3,7,4,6,5]
speed=[4,4,4,4,4,4]
print(carFleet(target, position, speed))
