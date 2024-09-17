from types import List 

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
    return []

temperatures = [30, 38, 30, 36, 35, 40, 28]

