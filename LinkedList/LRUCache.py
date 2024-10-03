class LRUCache: 

    def __init__(self, capacity: int):
        self.values = {}
        self.lhead = None
        self.ltail = None
        self.capacity = capacity

    def get(self, key: int) -> int: 
        if key in self.values:
            self.lhead, self.ltail = moveToEnd(self.lhead, self.ltail, self.values[key])
            return self.values[key].value
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values[key].value = value
            self.lhead, self.ltail = moveToEnd(self.lhead, self.ltail, self.values[key])
        else:
            if len(self.values) == self.capacity: 
                keyToBeRemoved = self.lhead.key
                self.lhead, self.ltail = removeHead(self.lhead, self.ltail)
                del self.values[keyToBeRemoved]
             
            new_node = Node(key, value)
            self.values[key] = new_node            
            
            if self.lhead is None: 
                self.lhead = new_node
                self.ltail = new_node
            else:
                self.ltail.next = new_node 
                new_node.prev = self.ltail
                self.ltail = new_node

    def printState(self):
        print(self.values)
        self.lhead.print()


class Node: 
    def __init__(self, key = 0, value = 0, next = None, prev = None):
        self.key = key
        self.value = value 
        self.next = next 
        self.prev = prev

    def insert(self, node):
        if self.next is None: 
            self.next = node
            node.prev = self
            return 
        
        self.next.insert(node)

    def print(self):

        print(self.value)

        if self.next is None: 
            print("==================")
            return 
        
        self.next.print()

    def find(self, value):

        if self.value == value: 
            return self

        if self.next is None: 
            return None
        
        return self.next.find(value)

def moveToEnd(head, tail, target_node):
    if head is None or tail == target_node:
        return head, tail
    
    if target_node == head:
        head = target_node.next
        head.prev = None
    else:
        if target_node.prev is not None:
            target_node.prev.next = target_node.next
        if target_node.next is not None:
            target_node.next.prev = target_node.prev

    target_node.next = None 
    target_node.prev = tail 

    if tail is not None:
        tail.next = target_node
    
    tail = target_node

    return head, tail

def removeHead(head, tail):
        if head is None: 
            return None, tail 

        if head.next is None: 
            head = None  
            tail = None  
            return head, tail

        head.next.prev = None
        head = head.next 

        return head, tail

# head = Node(1)
# head.insert(Node(2))
# head.insert(Node(3))
# head.insert(Node(4))
# head.insert(Node(5))
# head.print()
# moveToEnd(head, 3)
# head.print()
# head = removeHead(head)
# head.print()

# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# cache.printState()
# print(cache.get(1))
# cache.printState()
# cache.put(3, 3)
# cache.printState()
# print(cache.get(2))
# cache.put(4, 4)
# cache.printState()
# print(cache.get(1))

# cache = LRUCache(1)
# cache.put(2, 1)
# cache.printState()
# print(cache.get(2))
# cache.put(3, 2)
# cache.printState()
# print(cache.get(2))
# print(cache.get(3))

cache = LRUCache(2)
cache.put(1, 0)
cache.put(2, 2)
cache.printState()
print(cache.get(1))
cache.printState()
cache.put(3, 3)
cache.printState()
print(cache.get(2))
cache.put(4, 4)
cache.printState()
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
