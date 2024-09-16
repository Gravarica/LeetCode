from typing import List

def evalOp(op: str, a,b: int) -> int:
        if op == "+":
            return a + b
        if op == "*": 
            return a * b
        if op == "-":
            return a - b
        if op == "/": 
            return int(float(a) / b)

def evalRPN(tokens: List[str]) -> int:
    operators = ["+", "*", "-", "/"]

    stack = []

    for token in tokens: 
        if token in operators:
            second = stack.pop()
            first = stack.pop() 
            res = evalOp(token, first, second)
            print("res: " + str(res))
            stack.append(res)
        else:
            print("val: " + token)
            stack.append(int(token))

    return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
res = evalRPN(tokens)
print("Final result is: " + str(res))