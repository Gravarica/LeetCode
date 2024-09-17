from typing import List 

def dailyTemperaturesNSQUARED(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures) 
    for i in range(len(temperatures)):
        counter = 0
        for j in range(i + 1, len(temperatures)):
            counter += 1
            if temperatures[i] < temperatures[j]:
                result[i] = counter
                break
            
    return result

def dailyTemperaturesSTACK(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures) 
    stack = []
    for i in range(1, len(temperatures)): 
        print(stack[-1])
        while stack and stack[-1][1] < temperatures[i]:
            idx, val = stack.pop()
            result[idx] = i - idx
        stack.append((i, temperatures[i]))

    return result

temperatures = [30, 38, 30, 36, 35, 40, 28]

res = dailyTemperaturesSTACK(temperatures)
print(res)

