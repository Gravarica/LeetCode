def findArrayDuplicate(array):
    assert len(array) > 0

    slow = 0
    fast = 0

    while True:
        slow = array[slow]
        fast = array[array[fast]]
        if slow == fast:
            break

    print(slow)

    finder = 0
    while True: 
        slow = array[slow]
        finder = array[finder]

        if slow == finder: 
            return slow 
        
arr = [3, 1, 3, 4, 2]
num = findArrayDuplicate(arr)
print(num)
    